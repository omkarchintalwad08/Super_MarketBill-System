from datetime import datetime


class Item:
    def __init__(self, name, qty, price):
        self.item_name = name
        self.qty = qty
        self.price = price
        self.total = qty * price


class SuperMarketBill:
    # ---------------- Shop Details ----------------
    SHOP_NAME = "SMART MART SUPERMARKET"
    GSTIN = "GSTIN:14ABCD1234"
    SHOP_ADDRESS = "Latur, Maharashtra"

    def __init__(self, customer_name=None, items=None, cashier_name=None, counter_no=None):
        if customer_name is None:
            # Header Constructor
            print("\n======================================================")
            print(f"                {self.SHOP_NAME}")
            print(f"                   {self.GSTIN}")
            print(f"                  {self.SHOP_ADDRESS}")
            print("======================================================\n")
        else:
            # Billing Constructor
            self.customer_name = customer_name
            self.items = items
            self.cashier_name = cashier_name
            self.counter_no = counter_no

            self.total_items = len(items)

            now = datetime.now()
            self.bill_date = now.strftime("%d-%m-%Y %H:%M:%S")
            self.bill_no = "SM-" + now.strftime("%Y%m%d%H%M%S")

            self.calculate_bill()

    # ---------------- Bill Calculation ----------------
    def calculate_bill(self):
        self.total_amount = sum(item.total for item in self.items)

        self.discount10 = self.total_amount * 0.10 if self.total_amount > 1000 else 0

        after_discount = self.total_amount - self.discount10

        self.cgst = after_discount * 0.025
        self.sgst = after_discount * 0.025

        after_tax = after_discount + self.cgst + self.sgst

        self.final_discount = after_tax * 0.05

        self.net_amount = after_tax - self.final_discount
        self.saved_amount = self.discount10 + self.final_discount

    # ---------------- Bill Details ----------------
    def show_bill_details(self):
        print("                     BILL DETAILS")
        print("------------------------------------------------------")
        print(f"Customer Name : {self.customer_name}")
        print(f"Bill No       : {self.bill_no}")
        print(f"Bill Date     : {self.bill_date}")
        print(f"Cashier Name  : {self.cashier_name}")
        print(f"Counter No    : {self.counter_no}")
        print("------------------------------------------------------")

    # ---------------- Item Details ----------------
    def show_item_details(self):
        print(f"{'No':<5}{'Item':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")

        for i, item in enumerate(self.items, start=1):
            print(f"{i:<5}{item.item_name:<15}{item.qty:<8}"
                  f"{item.price:<10.2f}{item.total:<10.2f}")

    # ---------------- Bill Summary ----------------
    def show_bill_summary(self):
        print("------------------------------------------------------")
        print(f"{'Total Amount':<25}: Rs. {self.total_amount:.2f}")
        print(f"{'10% Discount':<25}: Rs. {self.discount10:.2f}")
        print(f"{'CGST (2.5%)':<25}: Rs. {self.cgst:.2f}")
        print(f"{'SGST (2.5%)':<25}: Rs. {self.sgst:.2f}")
        print(f"{'Final Discount':<25}: Rs. {self.final_discount:.2f}")
        print("------------------------------------------------------")
        print(f"{'Net Amount':<25}: Rs. {self.net_amount:.2f}")
        print(f"\nYOU HAVE SAVED : Rs. {self.saved_amount:.2f}")

    # ---------------- Payment ----------------
    def process_payment(self):
        print("\n-------------------- PAYMENT MODE --------------------")
        print("1. Cash")
        print("2. UPI")

        choice = int(input("Select option (1/2): "))

        if choice == 1:
            self.payment_mode = "CASH"
            self.paid_amount = float(input("Enter Paid Amount : Rs. "))
            self.change_to_return = self.paid_amount - self.net_amount
        else:
            self.payment_mode = "UPI"
            self.upi_id = input("Enter UPI ID : ")
            self.paid_amount = self.net_amount
            self.change_to_return = 0

    # ---------------- Payment Summary ----------------
    def show_payment_details(self):
        print("\n------------------ PAYMENT SUMMARY ------------------")
        print(f"{'Payment Mode':<20}: {self.payment_mode}")
        print(f"{'Paid Amount':<20}: Rs. {self.paid_amount:.2f}")

        if self.payment_mode == "CASH":
            print(f"{'Change Return':<20}: Rs. {self.change_to_return:.2f}")
        else:
            print(f"{'UPI ID':<20}: {self.upi_id}")

        print("------------------------------------------------------")
        print("         Thank you for shopping with us :)")
        print("======================================================")


# ---------------- Main Program ----------------

print("************* Supermarket Billing System *************\n")
print("----------- DATA ENTRY FOR BILL GENERATION -----------\n")

customer_name = input("Enter Customer Name : ")
cashier_name = input("Enter Cashier Name  : ")
counter_no = int(input("Enter Counter No    : "))
n = int(input("Enter Number of Items : "))

items = []

for i in range(n):
    print(f"\nDetail For Item {i + 1}:")
    name = input("Item Name : ")
    qty = int(input("Quantity  : "))
    price = float(input("Price     : "))
    items.append(Item(name, qty, price))

# Display Header
SuperMarketBill()

# Generate Bill
bill = SuperMarketBill(customer_name, items, cashier_name, counter_no)

bill.show_bill_details()
bill.show_item_details()
bill.show_bill_summary()
bill.process_payment()
bill.show_payment_details()

    
