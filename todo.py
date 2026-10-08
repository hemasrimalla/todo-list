"""
Simple Command-Line To-Do List Application
A beginner-friendly Python program demonstrating lists, loops,
functions, conditions, and user input validation.
"""


def add_task(tasks):
    """
    Prompt the user for a task description and append it to the task list.
    Validates that the task description is not empty.
    """
    task = input("\nEnter the task description: ").strip()

    # Validate that the user did not provide an empty string
    if not task:
        print("Error: Task description cannot be empty.")
        return

    # Add the valid task to our list
    tasks.append(task)
    print(f"Success: Task '{task}' added successfully!")


def view_tasks(tasks):
    """
    Display all tasks as a numbered list starting from 1.
    If the list is empty, print 'No tasks yet.'
    """
    print("\n--- To-Do List ---")
    # Check if the list contains any items
    if not tasks:
        print("No tasks yet.")
        return

    # Loop through tasks using enumerate to get 1-based index
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def update_task(tasks):
    """
    Prompt the user for a task number and a new description,
    then update the task at that position.
    Validates numeric input, index range, and empty text.
    """
    # Check if there are tasks to update
    if not tasks:
        print("\n--- Update Task ---")
        print("No tasks yet.")
        return

    # Display current tasks so the user can easily choose a task number
    view_tasks(tasks)

    # Prompt user for the task number to update
    task_input = input("\nEnter the task number to update: ").strip()

    # Use try/except to handle non-numeric inputs
    try:
        task_num = int(task_input)

        # Validate that the number is within the valid list range
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task description: ").strip()

            # Validate that the replacement text is not empty
            if not new_task:
                print("Error: Task description cannot be empty.")
                return

            # Update the task at the specified index (0-based)
            old_task = tasks[task_num - 1]
            tasks[task_num - 1] = new_task
            print(f"Success: Task {task_num} updated from '{old_task}' to '{new_task}'.")
        else:
            print(f"Error: Task number out of range. Please enter a number between 1 and {len(tasks)}.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid numeric task number.")


def remove_task(tasks):
    """
    Prompt the user for a task number and remove it from the list.
    Validates numeric input and index range.
    """
    # Check if there are tasks to remove
    if not tasks:
        print("\n--- Remove Task ---")
        print("No tasks yet.")
        return

    # Display current tasks so the user can see available numbers
    view_tasks(tasks)

    # Prompt user for the task number to remove
    task_input = input("\nEnter the task number to remove: ").strip()

    # Use try/except to handle non-numeric inputs
    try:
        task_num = int(task_input)

        # Validate that the number is within the valid list range
        if 1 <= task_num <= len(tasks):
            # pop() removes and returns the element at the specified index
            removed_task = tasks.pop(task_num - 1)
            print(f"Success: Task '{removed_task}' removed successfully!")
        else:
            print(f"Error: Task number out of range. Please enter a number between 1 and {len(tasks)}.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid numeric task number.")


def main():
    """
    Main function to run the interactive menu loop.
    Maintains the task list and routes user choices to the appropriate functions.
    """
    # List to store task descriptions
    tasks = []

    # Run the menu loop continuously until the user chooses to exit
    while True:
        print("\n=============================")
        print("      TO-DO LIST MENU        ")
        print("=============================")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Remove a task")
        print("5. Exit")
        print("=============================")

        choice = input("Enter your choice (1-5): ").strip()

        # Decision making with if / elif / else
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("\nGoodbye! Have a productive day.")
            break
        else:
            print("Error: Invalid menu choice. Please enter a number between 1 and 5.")


# Standard Python boilerplate to run main() when script is executed directly
if __name__ == "__main__":
    main()
