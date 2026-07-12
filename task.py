import os
import json

FILE_NAME = 'tasks.json'

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file) 
    except(json.JSONDecodeError, PermissionError):
        return []

def save_tasks(tasks):
    try:
        with open (FILE_NAME,"w") as file:
            json.dump(tasks,file, indent=4)
    except(PermissionError):
        print('Failed to save due to permission errors')

def add_tasks(tasks):
    description = input("Describe your task: ")
    if not description:
        print('You cannot enter an empty description')
    
    task_id = max([t['id']for t in tasks]) + 1 if tasks else 1
    
    new_task = {
        'id': task_id,
        'description' : description,
        'status': 'In Progress'
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task added Successfully! [ID: {task_id}]")

def view_tasks(tasks):
    if not tasks:
        print('You have no tasks in your list currently!')
        return
    print(f"{'ID':<6}{'Description':<36}{'Status':<15}")
    print("-"* 56)
    for task in tasks:
        icon = "⏳" if task["status"] ==  "In Progress" else "✅"
        print(f"{task['id']:<6}{task['description']:<36}{task['status']:<15}")
        print("===============================================================================")

def complete_task(tasks):
    if not tasks:
        print("No tasks in list currently!")
        return
    try:
        target_id = int(input('Enter the Id of the task you completed!: '))
    except ValueError:
        print('Invalid format, Please enter a valid ID')
        return
    
    for task in tasks:
        if target_id == task['id']:
            if task['status'] == 'Completed':
                print("You already completed this task!")
                return
            task['status'] ='Completed'
            save_tasks(tasks)
            print(f'✅ Task:{target_id} marked as completed!')
            return
    print('Could not find task with ID: {target_ID}')

def delete_task(tasks):
    if not tasks:
        print('No tasks in the list currently!')
        return
    try:
        target_id = int(input('Enter the Id of the target you would like to remove!: '))
    except ValueError:
        print('Invalid format! Please enter a valid ID')
        return
    for task in tasks:
        if target_id == task['id']:
            tasks.remove(task)
            save_tasks(task)
            print(f'Task:{target_id} has been deleted!')
            return
        print('Task with the provided target ID was not found!')
    
def main():
    print("Welcome to your personal Task Tracker")
    tasks = load_tasks()

    while True:
        print("\n===Main Menu===")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Delete Tasks")
        print("5. Exit")

        choice = int(input("Choose an Option 1-5: ").strip())
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_tasks(tasks)
        elif choice == 3:
            complete_task(tasks)
        elif choice == 4:
                delete_task(tasks)
        elif choice == 5:
            break
        else:
            print('Please enter a valid choice.')

if __name__ == "__main__":
    main()

