from generate_invoice import generate_purchase_invoice
from read import load_inventory

def add_medicienes():
    all_records = load_inventory()
    session_records = []

    print("Enter the name of the vendor:")
    vendor_name = input("Vendor Name:")

    while True:
        print("-" * 50)

        print("Enter the details of a new medicine:")
        name = input("Name: ")
        brand = input("Brand: ")

        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            rate_per_tablet = int(input("Rate per Tablet: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            rate_per_strip = int(input("Rate per Strip: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            number_in_one_strip = int(input("Number in one Strip: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        found = False

        for medicine in all_records:
            if medicine["Name"].lower() == name.lower() and medicine["Brand"].lower() == brand.lower():
                print("Medicine with this name and brand already exists.")

                medicine["Quantity"] += quantity
                print(f"Quantity updated to {medicine['Quantity']}")

                medicine["RatePerTablet"] = rate_per_tablet
                print(f"Rate per tablet updated to {medicine['RatePerTablet']}")

                medicine["RatePerStrip"] = rate_per_strip
                print(f"Rate per strip updated to {medicine['RatePerStrip']}")

                medicine["TabletPerStrip"] = number_in_one_strip
                print(f"Number in one strip updated to {medicine['TabletPerStrip']}")

                session_records.append({
                    "Name": medicine["Name"],
                    "Quantity": quantity,
                    "RatePerStrip": rate_per_strip
                })

                found = True
                break

        if not found:
            new_record = {
                "S.N.": get_medicine_no(),
                "Name": name,\
                "Brand": brand,
                "Quantity": quantity,
                "RatePerTablet": rate_per_tablet,
                "RatePerStrip": rate_per_strip,
                "TabletPerStrip": number_in_one_strip,
            }
            all_records.append(new_record)

            session_records.append({
                "Name": new_record["Name"],
                "Quantity": quantity,
                "RatePerStrip": rate_per_strip
            })


        save_inventory(all_records)
        is_continue = input("Do you want to add another medicine? (yes/no): ")
        if is_continue.lower() == 'yes':
            continue
        elif is_continue.lower() == 'no':
            break
        else:
            while True:
                print("Invalid input. Please enter yes or no.")
                is_continue = input("Do you want to add another medicine? (yes/no): ")
                if is_continue.lower() == 'yes':
                    continue
                elif is_continue.lower() == 'no':
                    break
                else:
                    continue
            break

    if session_records:
        generate_purchase_invoice(session_records, vendor_name)


def get_medicine_no():
    with open("data.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            return 1
        last_line = lines[-1]
        last_sn = int(last_line.split(",")[0].strip())
        return last_sn + 1


def save_inventory(data):
    with open("data.txt", "w") as file:
        for item in data:
            file.write(
                f"{item['S.N.']}, {item['Name']}, {item['Brand']}, {item['Quantity']}, "
                f"{item['RatePerTablet']}, {item['RatePerStrip']}, {item['TabletPerStrip']}\n"
            )
