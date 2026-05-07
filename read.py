def read_data():
    """
    Displays all medicine records stored in the inventory.
    """
    data = load_inventory()

    print("-" * 60, "Medical Inventory", "-" * 60)

    # Display table headings
    print(f"{"S.N.":<5}{'Name':<25} {'Brand':<20} {'Quanty':<20} {'Rate per Tablet':<20} {'Rate per Strip':<20} {'Tablet Per Strip':<20}")

    print("-" * 140)

    # Display each medicine record
    for i in data:
        print(f"{i['S.N.']:<5} {i['Name']:<25} {i['Brand']:<20} {i['Quantity']:<20} {i['RatePerTablet']:<20} {i['RatePerStrip']:<20} {i['TabletPerStrip']:<20}")

    print("-" * 140)


def load_inventory():
    """
    Loads medicine inventory data from the data file
    and returns it as a list of dictionaries.
    """
    data = []

    with open("data.txt", "r") as file:

        # Read each line from the file
        for line in file:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split comma-separated values
            parts = [p.strip() for p in line.split(",")]

            # Store medicine details in dictionary format
            data.append({
                "S.N.": parts[0],
                "Name": parts[1],
                "Brand": parts[2],
                "Quantity": int(parts[3]),
                "RatePerTablet": int(parts[4]),
                "RatePerStrip": int(parts[5]),
                "TabletPerStrip": int(parts[6]),
            })

    return data
