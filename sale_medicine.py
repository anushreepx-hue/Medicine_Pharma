from generate_invoice import generate_sales_invoice
from write import save_inventory
from read import load_inventory

def make_medicine_sales():

    inventory = load_inventory()
    bill_items = []
    customer_name = input("Enter a Customer Name: ")


    while True:
        print("\nAvailable Medicines:")
        for i, med in enumerate(inventory):
            print(f"{i+1}. {med['Name']} ({med['Brand']}) - Stock: {med['Quantity']}")

        try:
            choice = int(input("Select medicine (number): ")) - 1
        except ValueError:
            print("Invalid choice. Invalid input. Please enter a number.")
            continue

        if choice < 0 or choice >= len(inventory):
            print("Invalid choice")
            continue

        med = inventory[choice]

        print("\nSell by:")
        print("1. Tablet")
        print("2. Strip")

        try:
            sale_type = int(input("Choose option: "))
        except ValueError:
            print("Invalid input.")
            continue

        strip_size = med["TabletPerStrip"]

        if sale_type == 1:
            try:
                qty = int(input("Enter quantity (tablets): "))
            except ValueError:
                print("Invalid input.")
                continue

        elif sale_type == 2:
            try:
                strip_qty = int(input("Enter number of strips: "))
            except ValueError:
                print("Invalid input.")
                continue

            qty = strip_qty * strip_size

        else:
            print("Invalid option.")
            continue


        if qty > med["Quantity"]:
            print("Not enough stock!")
            continue

        med["Quantity"] -= qty

        strips = qty // strip_size

        discount = 0
        if is_discount_applicable(strips):
            discount = 0.05

        price = med["RatePerTablet"] * qty
        final_price = price - (price * discount)
        final_price_with_vat = add_vat(final_price)

        bill_items.append({
            "Name": med["Name"],
            "Quantity": qty,
            "Rate": med["RatePerTablet"],
            "Total": final_price_with_vat,
            "Discount": discount * 100,
            "Vat Amount": final_price_with_vat - final_price
        })

        cont = input("Add more? (yes/no): ")
        if cont.lower() == "no":
            break

    save_inventory(inventory)

    generate_sales_invoice(customer_name, bill_items)

def is_discount_applicable(strip):
    if strip >=2:
        return True
    return False


def add_vat(price):
    vat_rate = 0.13
    return price * (1 + vat_rate)

