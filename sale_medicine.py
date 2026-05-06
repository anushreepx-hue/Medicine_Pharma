from generate_invoice import generate_sales_invoice
from read import read_data

def make_medicine_sales():

    inventory = load_inventory()
    bill_items = []
    customer_name = input("Enter a Customer Name: ")


    while True:
        print("\nAvailable Medicines:")
        for i, med in enumerate(inventory):
            print(f"{i+1}. {med['Name']} ({med['Brand']}) - Stock: {med['Quantity']}")

        try:                                                          # ← add this
            choice = int(input("Select medicine (number): ")) - 1
        except ValueError:                                           # ← catch locally
            print("Invalid choice. Invalid input. Please enter a number.")
            continue

        if choice < 0 or choice >= len(inventory):
            print("Invalid choice")
            continue

        med = inventory[choice]

        try:                                                          # ← add this
            qty = int(input("Enter quantity (tablets): "))
        except ValueError:                                           # ← catch locally
            print("Invalid input. Please enter a number.")
            continue


        if qty > med["Quantity"]:
            print("Not enough stock!")
            continue

        med["Quantity"] -= qty

        strip_size = med["NumberInOneStrip"]
        strips = qty // strip_size

        discount = 0
        if is_discount_applicable(strips):
            discount = 0.1   # 10%

        price = med["RatePerTablet"] * qty
        final_price = price - (price * discount)

        bill_items.append({
            "Name": med["Name"],
            "Quantity": qty,
            "Rate": med["RatePerTablet"],
            "Total": final_price,
            "Discount": discount * 100
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


def load_inventory():
    data = []
    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = [p.strip() for p in line.split(",")]

            data.append({
                "S.N.": parts[0],
                "Name": parts[1],
                "Brand": parts[2],
                "Quantity": parts[3],
                "RatePerTablet": parts[4],
                "RatePerStrip": parts[5],
                "TabletPerStrip": parts[6],
            })
    return data


def save_inventory(data):
    with open("data.txt", "w") as file:
        for item in data:
            file.write(
                f"{item['S.N.']}, {item['Name']}, {item['Brand']}, {item['Quantity']}, "
                f"{item['RatePerTablet']}, {item['RatePerStrip']}, {item['TabletPerStrip']}\n"
            )
