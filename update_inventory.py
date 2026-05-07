from generate_invoice import generate_purchase_invoice
from read import load_inventory
from write import save_inventory


def update_inventory():
    """
    Updates the stock quantity of an existing medicine
    and generates a purchase invoice after restocking.
    """
    inventory = load_inventory()

    print("\nCurrent Inventory:")
    print("-" * 60)

    # Display all medicines in inventory
    for i, med in enumerate(inventory):
        print(f"{i+1}. {med['Name']} ({med['Brand']}) - Stock: {med['Quantity']}")

    # Get medicine selection from user
    try:
        choice = int(input("\nSelect medicine to restock (number): ")) - 1

    except ValueError:
        print("Invalid input.")
        return

    # Validate selected index
    if choice < 0 or choice >= len(inventory):
        print("Invalid selection.")
        return

    selected_med = inventory[choice]

    print(f"\nSelected: {selected_med['Name']} ({selected_med['Brand']})")
    print(f"Current Stock: {selected_med['Quantity']}")

    # Get quantity to add
    try:
        added_qty = int(input("Enter quantity to ADD: "))

    except ValueError:
        print("Invalid input.")
        return

    # Quantity must be positive
    if added_qty <= 0:
        print("Quantity must be positive.")
        return

    # Update medicine stock
    selected_med["Quantity"] += added_qty

    # Save updated inventory to file
    save_inventory(inventory)

    print(f"Stock updated successfully! New stock: {selected_med['Quantity']}")

    # Vendor name for invoice generation
    vendor_name = input("Enter Vendor Name for invoice: ")

    # Record used for invoice generation
    restock_record = [{
        "Name": selected_med["Name"],
        "Brand": selected_med["Brand"],
        "Quantity": added_qty,
        "RatePerStrip": selected_med["RatePerStrip"]
    }]

    generate_purchase_invoice(restock_record, vendor_name)
