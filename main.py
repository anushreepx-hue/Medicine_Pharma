from read import read_data
from write import add_medicienes
from sale_medicine import make_medicine_sales
from update_inventory import update_inventory


def main():
    """
    Main entry point of the Medical System.
    Displays menu options and handles user choices.
    """

    """read_data()"""

    while True:
        print("Welcome to the Medical System!")
        print("Please select an option:")
        print("1. View Medical Inventory")
        print("2. Add New Medicines to Inventory")
        print("3. Make Medicine Sales")
        print("4. Update Current Inventory")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            # Validate menu choice
            if(choice < 1 or choice > 5):
                print("Invalid choice. Please try again.")
                continue

            # Execute selected option
            match choice:

                case 1:
                    read_data()

                case 2:
                    add_medicienes()

                case 3:
                    make_medicine_sales()

                case 4:
                    update_inventory()

                case 5:
                    print("Exiting the Medical System. Goodbye!")
                    break

                case _:
                    print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Run the program
if __name__ == "__main__":
    main()
