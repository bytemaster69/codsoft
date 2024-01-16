import time
from colorama import Fore, Style 
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')
        self.show_loading_animation()

    def view_tasks(self):
        print("\nTasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        self.show_loading_animation()

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" marked as complete.')
        else:
            print("Invalid task index.")
        self.show_loading_animation()

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task index.")
        self.show_loading_animation()

    def show_loading_animation(self):
        print("Processing", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as complete: "))
            todo_list.complete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            print("Exiting ToDoList. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
