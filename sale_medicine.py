from generate_invoice import generate_sales_invoice
from read import read_data

def make_medicine_sales():
    print("Enter the name of the customer:")
    customer_name = input("Customer Name:")

    all_records = []
    while True:
        print("-" * 50)
        read_data()

        # all_records.append(new_record)
        is_continue = input("Do you want to add another medicine? (yes/no): ")
        if is_continue.lower() == 'no':
            break

    if all_records:
        generate_sales_invoice(customer_name, all_records)

