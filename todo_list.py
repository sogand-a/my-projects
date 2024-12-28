def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.append(task)
            print(f"'{task}' has been added to the to-do list.")

        elif choice == '2':
            print("\nYour tasks:")
            if not todo_list:
                print("The to-do list is empty.")
            else:
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task}")

        elif choice == '3':
            task_number = input("Enter the task number to remove: ")
            if task_number.isdigit() and 1 <= int(task_number) <= len(todo_list):
                removed_task = todo_list.pop(int(task_number) - 1)
                print(f"'{removed_task}' has been removed from the to-do list.")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
