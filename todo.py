import os

def display_menu():
    print("\nSimple To-Do List")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Clear Completed Tasks")
    print("5. Exit\n")

def view_tasks():
    if not os.path.exists("tasks.txt"):
        print("No tasks found!\n")
        return

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("\nTo-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
        else:
            print("No tasks found!\n")

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!\n")

def mark_completed():
    view_tasks()
    task_num = int(input("Enter the task number to mark as completed: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1] = "[Completed] " + tasks[task_num - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as completed!\n")
    else:
        print("Invalid task number\n")

def clear_completed():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    tasks = [task for task in tasks if not task.startswith("[Completed]\n")]
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)
    print("Completed tasks cleared!\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            clear_completed()
        elif choice == "5":
            print("Exiting the program...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
