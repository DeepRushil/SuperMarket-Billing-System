import os
import random
from tkinter import *
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1340x750+0+0")  # UI Dimensions
        self.root.configure(bg="#f0f0f0")  # Light Grey background
        self.root.title("Billing Software")  # Title

        # Title Heading
        title = Label(
            self.root,
            text="SuperMarket Billing System - Rushil Supermarket",
            bd=12,
            relief=FLAT,
            font=("Poppins", 20, "bold"),
            bg="#9e9e9e",
            fg="black",
        ).pack(fill=X)

        # =========================== Variables =========================
        # Snacks
        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.namkeen = IntVar()
        self.pasta = IntVar()

        # Grocery
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.dal = IntVar()
        self.tea = IntVar()
        self.atta = IntVar()

        # Beauty & Hygiene
        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()

        # Totals
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()

        # Bill Variables
        self.c_name = StringVar()  # Customer name
        self.bill_no = StringVar()  # Bill number
        x = random.randint(1000, 9999)  # Generate random number for bill
        self.bill_no.set(str(x))
        self.phone = StringVar()  # Customer Phone Number

        # =========================== Customer Details Label Frame =========================
        details = LabelFrame(
            self.root,
            text="Customer Details :",
            font=("Arial", 14, "bold"),
            bg="#f7f7f7",
            fg="black",
            relief=FLAT,
            bd=10,
        )
        details.place(x=0, y=80, relwidth=1)

        cust_name = Label(
            details, text="Customer Name:", font=("Arial", 13), bg="#f7f7f7", fg="black"
        ).grid(row=0, column=0, padx=15)
        cust_entry = Entry(
            details, borderwidth=2, width=30, textvariable=self.c_name
        ).grid(row=0, column=1, padx=8)

        contact_name = Label(
            details, text="Contact No.", font=("Arial", 13), bg="#f7f7f7", fg="black"
        ).grid(row=0, column=2, padx=10)
        contact_entry = Entry(
            details, borderwidth=2, width=30, textvariable=self.phone
        ).grid(row=0, column=3, padx=8)

        bill_name = Label(
            details, text="Bill.No.", font=("Arial", 13), bg="#f7f7f7", fg="black"
        ).grid(row=0, column=4, padx=10)
        bill_entry = Entry(
            details, borderwidth=2, width=30, textvariable=self.bill_no
        ).grid(row=0, column=5, padx=8)

        # =========================== Snacks Label Frame ===================================
        snacks = LabelFrame(
            self.root,
            text="Snacks",
            font=("Arial", 12, "bold"),
            bg="#f7f7f7",
            fg="black",
            relief=FLAT,
            bd=10,
        )
        snacks.place(x=5, y=180, height=400, width=325)
        self.create_snacks_section(snacks)

        # =========================== Grocery Label Frame ===================================
        grocery = LabelFrame(
            self.root,
            text="Grocery",
            font=("Arial", 12, "bold"),
            relief=FLAT,
            bd=10,
            bg="#f7f7f7",
            fg="black",
        )
        grocery.place(x=340, y=180, height=400, width=325)
        self.create_grocery_section(grocery)

        # =========================== Beauty and Hygiene Label Frame ===================================
        hygiene = LabelFrame(
            self.root,
            text="Beauty & Hygiene",
            font=("Arial", 12, "bold"),
            relief=FLAT,
            bd=10,
            bg="#f7f7f7",
            fg="black",
        )
        hygiene.place(x=677, y=180, height=400, width=325)
        self.create_hygiene_section(hygiene)

        # ================================ BILL AREA ===================================
        billarea = Frame(self.root, bd=10, relief=FLAT, bg="#f7f7f7")
        billarea.place(x=1010, y=180, width=330, height=400)

        bill_title = Label(
            billarea,
            text="Bill Area",
            font=("Arial", 17, "bold"),
            bd=7,
            relief=FLAT,
            bg="#f7f7f7",
            fg="black",
        ).pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Billing Menu
        billing_menu = LabelFrame(
            self.root,
            text="Billing Summary",
            font=("Arial", 12, "bold"),
            relief=FLAT,
            bd=10,
            bg="#f7f7f7",
            fg="black",
        )
        billing_menu.place(x=0, y=600, relwidth=1, height=150)

        # Total Snacks Price
        total_snacks = Label(
            billing_menu,
            text="Total Snacks Price",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="black",
        ).grid(row=0, column=0, padx=20)

        # Buttons
        btn_total = Button(
            billing_menu,
            text="Total",
            command=self.total,
            bg="#4caf50",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10,
        )
        btn_total.grid(row=1, column=0, padx=20, pady=20)

        btn_generate = Button(
            billing_menu,
            text="Generate Bill",
            command=self.generate_bill,
            bg="#2196f3",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10,
        )
        btn_generate.grid(row=1, column=1, padx=20, pady=20)

        btn_clear = Button(
            billing_menu,
            text="Clear",
            command=self.clear,
            bg="#f44336",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10,
        )
        btn_clear.grid(row=1, column=2, padx=20, pady=20)

        btn_exit = Button(
            billing_menu,
            text="Exit",
            command=self.exit_app,
            bg="#9e9e9e",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10,
        )
        btn_exit.grid(row=1, column=3, padx=20, pady=20)

    def create_snacks_section(self, frame):
        items = [
            ("Nutella Choco Spread", self.nutella),
            ("Noodles (1 Pack)", self.noodles),
            ("Lays (10Rs)", self.lays),
            ("Oreo (20Rs)", self.oreo),
            ("Chocolate Muffin", self.muffin),
            ("Cadbury Silk", self.silk),
            ("Namkeen (400g)", self.namkeen),
            ("Maggi Pasta", self.pasta),
        ]

        for i, (item, var) in enumerate(items):
            Label(
                frame,
                text=item,
                font=("Arial Black", 11),
                bg="#ffffff",
                fg="#6C3483",
            ).grid(row=i, column=0, pady=11)
            Entry(frame, borderwidth=2, width=15, textvariable=var).grid(
                row=i, column=1, padx=10
            )

    def create_grocery_section(self, frame):
        items = [
            ("Basmati Rice (1Kg)", self.rice),
            ("Sunflower Oil (1L)", self.oil),
            ("Sugar (1Kg)", self.sugar),
            ("Toor Dal (1Kg)", self.dal),
            ("Tea (500g)", self.tea),
            ("Wheat Atta (1Kg)", self.atta),
        ]

        for i, (item, var) in enumerate(items):
            Label(
                frame,
                text=item,
                font=("Arial Black", 11),
                bg="#ffffff",
                fg="#1E8449",
            ).grid(row=i, column=0, pady=11)
            Entry(frame, borderwidth=2, width=15, textvariable=var).grid(
                row=i, column=1, padx=10
            )

    def create_hygiene_section(self, frame):
        items = [
            ("Dettol Soap", self.soap),
            ("Loreal Shampoo", self.shampoo),
            ("Vaseline Lotion", self.lotion),
            ("Fair & Lovely Cream", self.cream),
            ("Shaving Foam", self.foam),
            ("Face Mask", self.mask),
            ("Hand Sanitizer", self.sanitizer),
        ]

        for i, (item, var) in enumerate(items):
            Label(
                frame,
                text=item,
                font=("Arial Black", 11),
                bg="#ffffff",
                fg="#E74C3C",
            ).grid(row=i, column=0, pady=11)
            Entry(frame, borderwidth=2, width=15, textvariable=var).grid(
                row=i, column=1, padx=10
            )

    def total(self):
        # Calculate totals for each section
        self.total_sna.set(f"Rs. {sum([self.nutella.get() * 120, self.noodles.get() * 15, self.lays.get() * 10, self.oreo.get() * 20, self.muffin.get() * 35, self.silk.get() * 70, self.namkeen.get() * 60, self.pasta.get() * 45])}")
        self.total_gro.set(f"Rs. {sum([self.rice.get() * 90, self.oil.get() * 110, self.sugar.get() * 40, self.dal.get() * 60, self.tea.get() * 150, self.atta.get() * 45])}")
        self.total_hyg.set(f"Rs. {sum([self.soap.get() * 30, self.shampoo.get() * 140, self.lotion.get() * 120, self.cream.get() * 100, self.foam.get() * 130, self.mask.get() * 50, self.sanitizer.get() * 80])}")

    def generate_bill(self):
        # Generate and display bill
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, f"\tRushil SuperMarket\n")
        self.txtarea.insert(END, f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END, f"\n====================================")
        self.txtarea.insert(END, f"\nProducts\t\tQty\tPrice")
        self.txtarea.insert(END, f"\n====================================")

        # Add products with prices to the bill area
        self.add_products_to_bill()

        # Display totals
        self.txtarea.insert(END, f"\n====================================")
        self.txtarea.insert(END, f"\nTotal Snacks Price: {self.total_sna.get()}")
        self.txtarea.insert(END, f"\nTotal Grocery Price: {self.total_gro.get()}")
        self.txtarea.insert(END, f"\nTotal Hygiene Price: {self.total_hyg.get()}")
        self.txtarea.insert(END, f"\n\n====================================")
        self.txtarea.insert(END, f"\nThanks for Shopping with us!")

    def add_products_to_bill(self):
        products = [
            ("Nutella Choco Spread", self.nutella, 120),
            ("Noodles", self.noodles, 15),
            ("Lays", self.lays, 10),
            ("Oreo", self.oreo, 20),
            ("Chocolate Muffin", self.muffin, 35),
            ("Cadbury Silk", self.silk, 70),
            ("Namkeen", self.namkeen, 60),
            ("Maggi Pasta", self.pasta, 45),
            ("Basmati Rice", self.rice, 90),
            ("Sunflower Oil", self.oil, 110),
            ("Sugar", self.sugar, 40),
            ("Toor Dal", self.dal, 60),
            ("Tea", self.tea, 150),
            ("Wheat Atta", self.atta, 45),
            ("Dettol Soap", self.soap, 30),
            ("Loreal Shampoo", self.shampoo, 140),
            ("Vaseline Lotion", self.lotion, 120),
            ("Fair & Lovely Cream", self.cream, 100),
            ("Shaving Foam", self.foam, 130),
            ("Face Mask", self.mask, 50),
            ("Hand Sanitizer", self.sanitizer, 80),
        ]

        for product_name, var, price in products:
            quantity = var.get()
            if quantity > 0:
                self.txtarea.insert(END, f"\n{product_name}\t\t{quantity}\t{quantity * price}")

    def clear(self):
        # Clear all entries and reset form
        self.txtarea.delete(1.0, END)
        self.c_name.set("")
        self.phone.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))

        # Reset all product quantities
        for var in [
            self.nutella,
            self.noodles,
            self.lays,
            self.oreo,
            self.muffin,
            self.silk,
            self.namkeen,
            self.pasta,
            self.rice,
            self.oil,
            self.sugar,
            self.dal,
            self.tea,
            self.atta,
            self.soap,
            self.shampoo,
            self.lotion,
            self.cream,
            self.foam,
            self.mask,
            self.sanitizer,
        ]:
            var.set(0)

        self.total_sna.set("")
        self.total_gro.set("")
        self.total_hyg.set("")

    def exit_app(self):
        self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
