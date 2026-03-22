def manage_tasks():
    tasks = []

    while True:
        print("")
        print("Task Menu:")
        print("1 - Add a task")
        print("2 - View all tasks")
        print("3 - Remove a task by number")
        print("4 - Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added")

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks")
            else:
                print("Tasks:")
                i = 0
                while i < len(tasks):
                    print(str(i + 1) + " - " + tasks[i])
                    i = i + 1

        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks to remove")
            else:
                print("Tasks:")
                i = 0
                while i < len(tasks):
                    print(str(i + 1) + " - " + tasks[i])
                    i = i + 1

                number = input("Enter task number to remove: ")

                if number.isdigit():
                    number = int(number)
                    if number >= 1 and number <= len(tasks):
                        tasks.pop(number - 1)
                        print("Task removed")
                    else:
                        print("Invalid number")
                else:
                    print("Please enter a number")

        elif choice == "4":
            return

        else:
            print("Invalid choice")

