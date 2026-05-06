
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

    print("---------Medical System---------")

    print(f"{"S.N.":<5}{'Name':<25} {'Brand':<20} {'Qty':<8} {'Tab Rate':<12} {'Strip Rate':<12} {'Per Strip':<10}")
    print("-" * 95)
    for i in data:
        print(f"{i['S.N.']:<5} {i['Name']:<25} {i['Brand']:<20} {i['Quantity']:<8} {i['RatePerTablet']:<12} {i['RatePerStrip']:<12} {i['NumberInOneStrip']:<10}")

    print("-" * 95)

