
def read_data():
    data = []
    with open("data.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            parts = [part.strip() for part in parts]
            if not line:
                continue

            records = {
                    "S.N.":parts[0],
                    "Name":parts[1],
                    "Brand":parts[2],
                    "Quantity":parts[3],
                    "RatePerTablet":parts[4],
                    "RatePerStrip":parts[5],
                    "NumberInOneStrip":parts[6],}

            data.append(records)

    print("-" * 60, "Medical Inventory", "-" * 60)

    print(f"{"S.N.":<5}{'Name':<25} {'Brand':<20} {'Quanty':<20} {'Rate per Tablet':<20} {'Rate per Strip':<20} {'Tablet Per Strip':<20}")
    print("-" * 140)
    for i in data:
        print(f"{i['S.N.']:<5} {i['Name']:<25} {i['Brand']:<20} {i['Quantity']:<20} {i['RatePerTablet']:<20} {i['RatePerStrip']:<20} {i['NumberInOneStrip']:<20}")

    print("-" * 140)

