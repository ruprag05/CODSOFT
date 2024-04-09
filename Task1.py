class Todo:
    def __init__(self, task, status="Pending"):
        self.task = task
        self.status = status

class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(Todo(task))

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.todos):
            self.todos[task_index].status = "Done"
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if not self.todos:
            print("No tasks yet!")
            return
        print("To-Do List:")
        for i, todo in enumerate(self.todos):
            print(f"{i + 1}. [{todo.status}] {todo.task}")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Mark Task as Done\n3. Display Tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            task_index = int(input("Enter task index to mark as done: ")) - 1
            todo_list.mark_done(task_index)
            print("Task marked as done!")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
