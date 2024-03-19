class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task):
        """Remove a task from the list"""
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")

    def show_tasks(self):
        """Display all tasks in the list"""
        if self.tasks:
            print("Tasks in the To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the To-Do List.")

def main():
    todo_list = TodoList()

    while True:
        print("\n==== TO-DO LIST APP ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
