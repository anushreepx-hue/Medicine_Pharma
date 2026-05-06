from read import read_data
from write import add_medicienes
from sale_medicine import make_medicine_sales

def main():
    """read_data()"""
    while True:
        print("Welcome to the Medical System!")
        print("Please select an option:")
        print("1. View Medical Inventory")
        print("2. Add New Medicines to Inventory")
        print("3. Make Medicine Sales")
        print("4. Exit")


        try:
            choice = int(input("Enter your choice: "))

            if(choice < 1 or choice > 4):
                print("Invalid choice. Please try again.")
                continue
            match choice:
                case 1 :
                    read_data()
                case 2 :
                    add_medicienes()
                case 3:
                    make_medicine_sales()

                case 4:
                    print("Exiting the Medical System. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

