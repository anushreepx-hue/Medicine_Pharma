from generate_invoice import generate_purchase_invoice
from read import load_inventory
from write import save_inventory

def update_inventory():
    inventory = load_inventory()

    print("\nCurrent Inventory:")
    print("-" * 60)
    for i, med in enumerate(inventory):
        print(f"{i+1}. {med['Name']} ({med['Brand']}) - Stock: {med['Quantity']}")

    try:
        choice = int(input("\nSelect medicine to restock (number): ")) - 1
    except ValueError:
        print("Invalid input.")
        return

    if choice < 0 or choice >= len(inventory):
        print("Invalid selection.")
        return

    selected_med = inventory[choice]

    print(f"\nSelected: {selected_med['Name']} ({selected_med['Brand']})")
    print(f"Current Stock: {selected_med['Quantity']}")

    try:
        added_qty = int(input("Enter quantity to ADD: "))
    except ValueError:
        print("Invalid input.")
        return

    if added_qty <= 0:
        print("Quantity must be positive.")
        return

    selected_med["Quantity"] += added_qty

    save_inventory(inventory)

    print(f"Stock updated successfully! New stock: {selected_med['Quantity']}")

    vendor_name = input("Enter Vendor Name for invoice: ")

    restock_record = [{
        "Name": selected_med["Name"],
        "Quantity": added_qty,
        "RatePerStrip": selected_med["RatePerStrip"]
    }]

    generate_purchase_invoice(restock_record, vendor_name)
