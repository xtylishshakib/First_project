tasks = []
while True:
    a = int(input('''
    1. Add Task
    2. View Tasks
    3. Delete Tasks
    4. Exit
    Enter a number (1-4): '''))

    if a == 1:
        b = input("Enter a task: ")
        tasks.append(b)
        print("Task added")

    elif a == 2:
        if not tasks:
            print("Task list is empty.")
        else:
            print("\nYour tasks:")
            counter = 1
            for task in tasks:
                print(f"{counter}. {task}")
                counter += 1
                
    elif a == 3:
        if not tasks:
            print("Task list is empty, nothing to delete.")
        else:

            try:
                delete_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= delete_index < len(tasks):
                    deleted_task = tasks.pop(delete_index)
                    print(f"Deleted task: {deleted_task}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif a == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")