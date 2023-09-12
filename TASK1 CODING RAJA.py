class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)

    def mark_task_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True
class TaskPriority:
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
class TaskPriority:
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
def display_tasks(todo_list):
    for task in todo_list.tasks:
        status = "Completed" if task.completed else "Not Completed"
        print(f"Title: {task.title}")
        print(f"Priority: {task.priority}")
        print(f"Due Date: {task.due_date}")
        print(f"Status: {status}")
def save_tasks_to_file(todo_list, file_name):
    with open(file_name, 'w') as file:
        for task in todo_list.tasks:
            file.write(f"{task.title},{task.priority},{task.due_date},{task.completed}\n")

def load_tasks_from_file(file_name):
    todo_list = ToDoList()
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 4:
                    title, priority, due_date, completed = data
                    task = Task(title, priority, due_date)
                    if completed == 'True':
                        task.completed = True
                    todo_list.add_task(task)
    except FileNotFoundError:
        pass
    return todo_list
def main():
    todo_list = load_tasks_from_file('tasks.txt')
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, priority, due_date)
            todo_list.add_task(task)
        elif choice == '2':
            title = input("Enter task title to remove: ")
            todo_list.remove_task(title)
        elif choice == '3':
            title = input("Enter task title to mark as completed: ")
            todo_list.mark_task_completed(title)
        elif choice == '4':
            display_tasks(todo_list)
        elif choice == '5':
            save_tasks_to_file(todo_list, 'tasks.txt')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

