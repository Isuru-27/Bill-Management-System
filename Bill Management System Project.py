from datetime import datetime

class DCItem:
    def __init__(self, name, price, quantity, discount=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

class DCBill:
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.items = []
        self.datetime = datetime.now()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            item_total = (item.price * item.quantity) - (item.price * item.quantity * item.discount / 100)
            total += item_total
        return total

    def print_bill(self, cash):
        print("____________________Denim Center____________________\n________________Sri Lanka's Unique Brand________________\n_________#156, Hemapala Munidasa Road, Welimada._________\n_____________T : 057-8945635 | E : dc@sltnet.lk_____________")
        print(f"Date: {self.datetime.strftime('%Y-%m-%d                                                         %I:%M:%S%p')}")
        print("----------------------------------------------------------------------------------")
        print(f"Cashier: {self.cashier_name}")
        print("----------------------------------------------------------------------------------")
        print("Item Name    Price     Quantity   Discount")
        print("----------------------------------------------------------------------------------")
        for item in self.items:
            print(f"{item.name:12} {item.price:8.2f} {item.quantity:8} {item.discount:8}%")
        print("----------------------------------------------------------------------------------")
        total = self.calculate_total()
        print(f"Sub Total: {total:.2f}")
        print(f"Cash: {cash:.2f}")
        print("----------------------------------------------------------------------------------")
        balance = cash - total
        print(f"Balance: {balance:.2f}")
        print(f"Number of items: {len(self.items)}")
        print("----------------------------------------------------------------------------------")
        print(" WE ARE HAPPY TO EXCHANGE PRODUCTS \n     RETURNED IN SALEABLE CONDITION,\nALONG WITH THE RECEIPT, AT ANY OF OUR\n              DENIM CENTER OUTLETS")
        print("----------------------------------------------------------------------------------")
        print("     SHOP ONLINE AT www.denimcenter.lk\n   THANK YOU FOR SHOPPING WITH US\nSHARE YOUR THOUGHT AT feedback@dc.lk")


def main():
    cashier_name = input("Enter cashier name: ")
    bill = DCBill(cashier_name)
    choice = ""
    while choice != "5":
        print("\n--- Welcome to DC---")
        print("1. Add item")
        print("2. Remove item")
        print("3. Calculate total")
        print("4. Print bill")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            discount = float(input("Enter item discount percentage: "))
            item = DCItem(name, price, quantity, discount)
            bill.add_item(item)
            print("Item added successfully!")

        elif choice == "2":
            if len(bill.items) == 0:
                print("No items in the bill.")
                continue
            print("Items in the bill:")
            for i, item in enumerate(bill.items):
                print(f"{i+1}. {item.name} ({item.quantity})")
            index = int(input("Enter the index of the item to remove: "))
            if index < 1 or index > len(bill.items):
                print("Invalid index.")
                continue
            item = bill.items[index - 1]
            bill.remove_item(item)
            print("Item removed successfully!")

        elif choice == "3":
            total = bill.calculate_total()
            print(f"Total: {total}")

        elif choice == "4":
            cash = float(input("Enter cash payment: "))
            bill.print_bill(cash)

        elif choice == "5":
            print("Exiting...")

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

