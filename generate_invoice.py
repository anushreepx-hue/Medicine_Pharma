import os
import datetime


def generate_purchase_invoice(records, vendor_name):
    filename = create_file("purchase_" + vendor_name, "purchase_invoices")
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    total = 0
    with open(filename, "w") as file:
        file.write("============================================================================\n")
        file.write(f"Purchase Invoice\n")
        file.write("============================================================================\n")
        file.write(f"Vendor: {vendor_name}\n")
        file.write(f"Date: {date}\n")
        file.write("-" * 120 + "\n")

        file.write(f"{'Name':<40}{'Qty':<20}{'Rate':<20}{'Total':<20}\n")
        file.write("-" * 120 + "\n")

        for item in records:
            qty = int(item["Quantity"])
            rate = float(item["RatePerStrip"])
            item_total = qty * rate
            total += item_total

            file.write(f"{item['Name']:<40}{qty:<20}{rate:<20}{item_total:<20}\n")

        file.write("-" * 120 + "\n")
        file.write(f"{'Grand Total:':<80}{total}\n")

    print("Purchase invoice generated!")

def generate_sales_invoice(customer, items):
    filename = create_file("sales_" + customer, "sales_invoices")

    grand_total = 0
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    with open(filename, "w") as f:
        f.write("============================================================================\n")
        f.write(f"Sales Invoice\n")
        f.write("============================================================================\n")
        f.write(f"Customer: {customer}\n")
        f.write(f"Date: {date}\n")
        f.write("-" * 120 + "\n")

        f.write(f"{'Name':<40}{'Qty':<10}{'Rate':<20}{'Disc%':<10}{'Total':<20}\n")
        f.write("-" * 120 + "\n")

        for item in items:
            f.write(f"{item['Name']:<40}{item['Quantity']:<10}{item['Rate']:<20}{item['Discount']:<10}{item['Total']:<20}\n")
            grand_total += item["Total"]
        f.write("-" * 120 + "\n")

        total_vat = sum(i["Vat Amount"] for i in items)
        f.write(f"{'VAT:':<80}{total_vat:<20}\n")
        f.write(f"{'Grand Total:':<80}{grand_total}\n")

    print("Invoice generated!")



def create_file(user_name, folder):
    os.makedirs(folder, exist_ok=True)
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    day= datetime.datetime.now().day
    hour= datetime.datetime.now().hour
    minute= datetime.datetime.now().minute
    second= datetime.datetime.now().second

    filename = user_name + "_" + str(year)+str(month)+str(day)+"_"+str(hour)+str(minute)+str(second) + ".txt"
    full_path = os.path.join(folder, filename)

    return full_path


# def display(file):
#     filedata= open(file)
#     print(file)
#     print(filedata.read())
#     filedata.close()
# display(file)
