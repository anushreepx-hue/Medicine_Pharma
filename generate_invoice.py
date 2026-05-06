import datetime


def generate_purchase_invoice(records, vendor_name):
    filename = create_file("purchase_" + vendor_name)

    total = 0
    with open(filename, "w") as file:
        file.write("====== PURCHASE INVOICE ======\n")
        file.write(f"Vendor: {vendor_name}\n")
        file.write("-" * 50 + "\n")

        file.write(f"{'Name':<20}{'Qty':<10}{'Rate':<10}{'Total':<10}\n")
        file.write("-" * 50 + "\n")

        for item in records:
            qty = int(item["Quantity"])
            rate = float(item["RatePerStrip"])
            item_total = qty * rate
            total += item_total

            file.write(f"{item['Name']:<20}{qty:<10}{rate:<10}{item_total:<10}\n")

        file.write("-" * 50 + "\n")
        file.write(f"{'Grand Total:':<30}{total}\n")

    print("Purchase invoice generated!")

def generate_sales_invoice(customer, items):
    filename = create_file("sales_" + customer)

    grand_total = 0

    with open(filename, "w") as f:
        f.write("====== SALES INVOICE ======\n")
        f.write(f"Customer: {customer}\n")
        f.write("-" * 60 + "\n")

        f.write(f"{'Name':<15}{'Qty':<5}{'Rate':<10}{'Disc%':<8}{'Total':<10}\n")
        f.write("-" * 60 + "\n")

        for item in items:
            f.write(f"{item['Name']:<15}{item['Quantity']:<5}{item['Rate']:<10}{item['Discount']:<8}{item['Total']:<10}\n")
            grand_total += item["Total"]

        f.write("-" * 60 + "\n")
        f.write(f"{'Grand Total:':<40}{grand_total}\n")

    print("Invoice generated!")



def create_file(user_name):
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    day= datetime.datetime.now().day
    hour= datetime.datetime.now().hour
    minute= datetime.datetime.now().minute
    second= datetime.datetime.now().second

    filename = user_name + "_" + str(year)+str(month)+str(day)+"_"+str(hour)+str(minute)+str(second) + ".txt"

    file= open(filename,"w")
    file.write("This is a uniquely created file.")
    file.close()
    return filename


# def display(file):
#     filedata= open(file)
#     print(file)
#     print(filedata.read())
#     filedata.close()
# display(file)
