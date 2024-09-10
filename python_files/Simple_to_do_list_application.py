# Program to create a simple to-do list

# Initialize an empty to-do list
todo_list = []

# Function to add a task
def add_task(task):
    todo_list.append(task)

# Function to remove a task
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)

# Function to display tasks
def show_tasks():
    if todo_list:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks in the list")

# Main menu
while True:
    print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid option")
