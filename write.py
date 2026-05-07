from generate_invoice import generate_purchase_invoice
from read import load_inventory
from generate_invoice import generate_purchase_invoice


def add_medicienes():
    """
    Adds new medicines to the inventory or updates existing stock.
    Also generates a purchase invoice for the session.
    """
    all_records = load_inventory()
    session_records = []

    # Get vendor name
    while True:
        vendor_name = input("Vendor Name: ").strip()
        if vendor_name:
            break
        print("Vendor name cannot be empty.")

    print("-" * 50)

    while True:

        # Medicine name validation
        while True:
            name = input("Name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        # Brand validation
        while True:
            brand = input("Brand: ").strip()
            if brand:
                break
            print("Brand cannot be empty.")

        # Number of tablets in one strip
        while True:
            try:
                number_in_one_strip = int(input("Number in one Strip: "))
                if number_in_one_strip > 0:
                    break
                print("Must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Choose whether stock is entered as tablets or strips
        while True:
            try:
                stock_type = int(input("\nChoose stock type (1: Tablet, 2: Strip): "))
                if stock_type in (1, 2):
                    break
                print("Choose only 1 or 2.")
            except ValueError:
                print("Invalid input.")

        # Quantity validation
        if stock_type == 1:
            while True:
                try:
                    quantity = int(input("Quantity (tablets): "))
                    if quantity > 0:
                        break
                    print("Must be greater than 0.")
                except ValueError:
                    print("Invalid input.")

        else:
            while True:
                try:
                    strip_quantity = int(input("Quantity (strips): "))
                    if strip_quantity > 0:
                        break
                    print("Must be greater than 0.")
                except ValueError:
                    print("Invalid input.")

            # Convert strips to total tablet quantity
            quantity = strip_quantity * number_in_one_strip

        # Tablet price validation
        while True:
            try:
                rate_per_tablet = int(input("Rate per Tablet: "))
                if rate_per_tablet >= 0:
                    break
                print("Rate cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Strip price validation
        while True:
            try:
                rate_per_strip = int(input("Rate per Strip: "))
                if rate_per_strip >= 0:
                    break
                print("Rate cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        found = False

        # Check if medicine already exists
        for medicine in all_records:
            if medicine["Name"].lower() == name.lower() and medicine["Brand"].lower() == brand.lower():
                print("Medicine already exists. Updating stock...")

                medicine["Quantity"] += quantity
                medicine["RatePerTablet"] = rate_per_tablet
                medicine["RatePerStrip"] = rate_per_strip
                medicine["TabletPerStrip"] = number_in_one_strip

                # Store session data for invoice generation
                session_records.append({
                    "Name": medicine["Name"],
                    "Brand": medicine["Brand"],
                    "Quantity": quantity,
                    "RatePerStrip": rate_per_strip
                })

                found = True
                break

        # Add new medicine if not found
        if not found:
            new_record = {
                "S.N.": get_medicine_no(),
                "Name": name,
                "Brand": brand,
                "Quantity": quantity,
                "RatePerTablet": rate_per_tablet,
                "RatePerStrip": rate_per_strip,
                "TabletPerStrip": number_in_one_strip,
            }

            all_records.append(new_record)

            session_records.append({
                "Name": new_record["Name"],
                "Brand": new_record["Brand"],
                "Quantity": quantity,
                "RatePerStrip": rate_per_strip
            })

        # Ask user whether to continue adding medicines
        while True:
            is_continue = input("Add another medicine? (yes/no): ").strip().lower()

            if is_continue == "yes":
                break

            elif is_continue == "no":
                save_inventory(all_records)

                if session_records:
                    generate_purchase_invoice(session_records, vendor_name)

                return

            else:
                print("Please enter only yes or no.")


def get_medicine_no():
    """
    Returns the next serial number for a new medicine record.
    """
    with open("data.txt", "r") as file:
        lines = file.readlines()

        if not lines:
            return 1

        last_line = lines[-1]
        last_sn = int(last_line.split(",")[0].strip())

        return last_sn + 1


def save_inventory(data):
    """
    Saves updated inventory data to the data file.
    """
    with open("data.txt", "w") as file:
        for item in data:
            file.write(
                f"{item['S.N.']}, {item['Name']}, {item['Brand']}, {item['Quantity']}, "
                f"{item['RatePerTablet']}, {item['RatePerStrip']}, {item['TabletPerStrip']}\n"
            )
