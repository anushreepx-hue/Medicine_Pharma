from generate_invoice import generate_purchase_invoice, generate_sales_invoice

def write_data(new_record):
    with open("data.txt", "a") as file:
        file.write(f"{new_record['S.N.']}, {new_record['Name']}, {new_record['Brand']}, {new_record['Quantity']}, {new_record['RatePerTablet']}, {new_record['RatePerStrip']}, {new_record['NumberInOneStrip']}\n")
    print("Record added successfully.")



def add_medicienes():
    all_records = []
    print("Enter the name of the vendor:")
    vendor_name = input("Vendor Name:")

    while True:
        print("-" * 50)

        print("Enter the details of a new medicine:")
        name = input("Name: ")
        brand = input("Brand: ")
        quantity = input("Quantity: ")
        rate_per_tablet = input("Rate per Tablet: ")
        rate_per_strip = input("Rate per Strip: ")
        number_in_one_strip = input("Number in one Strip: ")
        new_record = {
            "S.N.": get_medicine_no(),
            "Name": name,\
            "Brand": brand,
            "Quantity": quantity,
            "RatePerTablet": rate_per_tablet,
            "RatePerStrip": rate_per_strip,
            "NumberInOneStrip": number_in_one_strip,
        }
        write_data(new_record)
        all_records.append(new_record)
        is_continue = input("Do you want to add another medicine? (yes/no): ")
        if is_continue.lower() == 'no':
            break

    if all_records:
        generate_purchase_invoice(all_records, vendor_name)


def get_medicine_no():
    with open("data.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            return 1
        last_line = lines[-1]
        last_sn = int(last_line.split(",")[0].strip())
        return last_sn + 1

