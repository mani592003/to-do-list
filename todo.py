from colorama import init, Fore, Style
init(autoreset=True)
import json
import os

DATA_FILE = "tasks.json"

# Load tasks from file (if it exists)
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        todo_list = json.load(f)
else:
    todo_list = []

# Save tasks to file
def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(todo_list, f)

def show_menu():
    print(Fore.CYAN + "\n--- TO-DO LIST MENU ---")
    print(Fore.YELLOW + "1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Exit")

    
def view_tasks():
    if not todo_list:
        print(Fore.RED + "Your to-do list is empty.")
    else:
        print(Fore.CYAN + "\nYour Tasks:")
        for idx, task in enumerate(todo_list, 1):
            status = Fore.GREEN + "✔" if task['done'] else Fore.RED + "✘"
            print(f"{Fore.YELLOW}{idx}. {task['title']} [{status}]")

    
def add_task():
    title = input("Enter task: ")
    todo_list.append({'title': title, 'done': False})
    save_tasks()
    print(Fore.GREEN + "Task added.")


def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 0 < task_no <= len(todo_list):
            todo_list[task_no - 1]['done'] = True
            save_tasks()
            print(Fore.GREEN + "Task marked as done.")

        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(todo_list):
            todo_list.pop(task_no - 1)
            save_tasks()
            print(Fore.GREEN + "Task deleted.")

        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def edit_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to edit: "))
        if 0 < task_no <= len(todo_list):
            new_title = input("Enter new task title: ")
            todo_list[task_no - 1]['title'] = new_title
            save_tasks()
            print(Fore.GREEN + "Task updated.")

        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        edit_task()
    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
