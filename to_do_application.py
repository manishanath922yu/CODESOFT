import json
import os

# File to store the to-do list
TODO_FILE = 'todo_list.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task."""
    task_id = str(len(tasks) + 1)
    description = input("Enter the task description: ")
    tasks[task_id] = {'description': description, 'completed': False}
    print(f"Task '{description}' added with ID {task_id}.")

def update_task(tasks):
    """Update an existing task."""
    task_id = input("Enter the task ID to update: ")
    if task_id in tasks:
        print(f"Current description: {tasks[task_id]['description']}")
        new_description = input("Enter new description (leave blank to keep current): ")
        if new_description:
            tasks[task_id]['description'] = new_description
        mark_complete = input("Mark as completed? (yes/no): ").lower()
        if mark_complete == 'yes':
            tasks[task_id]['completed'] = True
        elif mark_complete == 'no':
            tasks[task_id]['completed'] = False
        else:
            print("Invalid input. Task not updated.")
        print(f"Task {task_id} updated.")
    else:
        print("Task ID not found.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            status = "Completed" if task['completed'] else "Pending"
            print(f"ID: {task_id} | Description: {task['description']} | Status: {status}")

def remove_task(tasks):
    """Remove a task."""
    task_id = input("Enter the task ID to remove: ")
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} removed.")
    else:
        print("Task ID not found.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new task")
        print("2. Update an existing task")
        print("3. View all tasks")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
