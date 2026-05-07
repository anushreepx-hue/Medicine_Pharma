from generate_invoice import generate_sales_invoice
from write import save_inventory
from read import load_inventory


def make_medicine_sales():
    """
    Handles medicine sales, updates inventory stock,
    applies discounts and VAT, and generates a sales invoice.
    """

    inventory = load_inventory()
    bill_items = []

    # Get customer name
    customer_name = input("Enter a Customer Name: ")

    while True:
        print("\nAvailable Medicines:")

        # Display available medicines
        for i, med in enumerate(inventory):
            print(f"{i+1}. {med['Name']} ({med['Brand']}) - Stock: {med['Quantity']}")

        # Select medicine
        try:
            choice = int(input("Select medicine (number): ")) - 1

        except ValueError:
            print("Invalid choice. Invalid input. Please enter a number.")
            continue

        # Validate selected medicine
        if choice < 0 or choice >= len(inventory):
            print("Invalid choice")
            continue

        med = inventory[choice]

        print("\nSell by:")
        print("1. Tablet")
        print("2. Strip")

        # Select sales type
        try:
            sale_type = int(input("Choose option: "))

        except ValueError:
            print("Invalid input.")
            continue

        strip_size = med["TabletPerStrip"]

        # Sale by tablet
        if sale_type == 1:
            try:
                qty = int(input("Enter quantity (tablets): "))

            except ValueError:
                print("Invalid input.")
                continue

        # Sale by strip
        elif sale_type == 2:
            try:
                strip_qty = int(input("Enter number of strips: "))

            except ValueError:
                print("Invalid input.")
                continue

            # Convert strips to tablet quantity
            qty = strip_qty * strip_size

        else:
            print("Invalid option.")
            continue

        # Check stock availability
        if qty > med["Quantity"]:
            print("Not enough stock!")
            continue

        # Reduce stock after successful sale
        med["Quantity"] -= qty

        # Calculate equivalent strip count
        strips = qty // strip_size

        # Apply discount if eligible
        discount = 0

        if is_discount_applicable(strips):
            discount = 0.05

        # Price calculations
        price = med["RatePerTablet"] * qty
        final_price = price - (price * discount)
        final_price_with_vat = add_vat(final_price)

        # Store item details for invoice
        bill_items.append({
            "Name": med["Name"],
            "Brand": med["Brand"],
            "Quantity": qty,
            "Rate": med["RatePerTablet"],
            "Total": final_price_with_vat,
            "Discount": discount * 100,
            "Vat Amount": final_price_with_vat - final_price
        })

        # Ask whether user wants to continue
        cont = input("Add more? (yes/no): ")

        if cont.lower() == "no":
            break

    # Save updated inventory
    save_inventory(inventory)

    # Generate final sales invoice
    generate_sales_invoice(customer_name, bill_items)


def is_discount_applicable(strip):
    """
    Returns True if discount is applicable.
    Discount is applied for 2 or more strips.
    """
    if strip >= 2:
        return True

    return False


def add_vat(price):
    """
    Adds 13% VAT to the given price.
    """
    vat_rate = 0.13

    return price * (1 + vat_rate)
