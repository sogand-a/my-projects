def display_menu():
    print("\nShopping List Manager")
    print("1. Add item to shopping list")
    print("2. View shopping list")
    print("3. Remove item from shopping list")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")

        elif choice == '2':
            print("\nYour shopping list:")
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == '3':
            item_number = input("Enter the item number to remove: ")
            if item_number.isdigit() and 1 <= int(item_number) <= len(shopping_list):
                removed_item = shopping_list.pop(int(item_number) - 1)
                print(f"{removed_item} has been removed from the shopping list.")
            else:
                print("Invalid item number.")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
