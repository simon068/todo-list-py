import datetime
import json

class TodoList:
    def __init__(self):
        self.todos = []
        self.load_from_file() 

    def load_from_file(self):
        try:
            with open('todos.json', 'r') as file:
                self.todos = json.load(file)
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open('todos.json', 'w') as file:
            json.dump(self.todos, file)

    def add_task(self, task, priority=0, deadline=None):

        task_data = {
            'task': task,
            'priority': priority,
            'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'deadline': deadline
        }
        self.todos.append(task_data)
        self.save_to_file()

    def remove_task(self, index):
        try:
            del self.todos[index]
            self.save_to_file()
            print("Task removed successfully.")
        except IndexError:
            print("Task not found in the list.")

    def display_tasks(self):
        if self.todos:
            print("Todo List:")
            for index, task in enumerate(sorted(self.todos, key=lambda x: x['priority']), start=1):
                print(f"{index}. {task['task']} - Priority: {task['priority']}")
                if task['deadline']:
                    print(f"   Deadline: {task['deadline']}")
                print(f"   Created At: {task['created_at']}   Updated At: {task['updated_at']}")
        else:
            print("Todo List is empty.")

    def search_tasks(self, keyword):
        found_tasks = [task for task in self.todos if keyword.lower() in task['task'].lower()]
        if found_tasks:
            print("Found tasks:")
            for task in found_tasks:
                print(f"- {task['task']}")
        else:
            print("No tasks found.")

def main():
    print("Welcome to Todo List Application!")
    print("This application allows you to manage your tasks efficiently.\n")
    input("Press Enter to continue...")

    todo_list = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Search Tasks")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            priority = int(input("Enter the priority (0-5): "))
            deadline = input("Enter the deadline (optional, format: YYYY-MM-DD HH:MM): ")
            if deadline:
                deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M")
            todo_list.add_task(task, priority, deadline)
        elif choice == '2':
            index = input("Enter the index of the task to remove: ")
            if index.isdigit():
                index = int(index) - 1 
                if 0 <= index < len(todo_list.todos):
                    todo_list.remove_task(index)
                else:
                    print("Invalid index. Please enter a valid index.")
            else:
                print("Invalid index. Please enter a valid index.")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            keyword = input("Enter keyword to search: ")
            todo_list.search_tasks(keyword)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()