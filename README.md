# Command-Line To-Do List Application

A clean, beginner-friendly, menu-driven command-line to-do list manager written in pure Python 3 without any external dependencies.

This project is designed as an educational example to demonstrate fundamental programming concepts including Python lists, `while` loops, conditional logic, modular functions, and robust input validation.

---

## 📌 Features

1. **Add a Task (`add_task`)**: Prompts for a task description and appends it to the list. Prevents empty or whitespace-only inputs.
2. **View All Tasks (`view_tasks`)**: Displays all tasks as a human-friendly numbered list (starting at `1`). Displays `"No tasks yet."` when the list is empty.
3. **Update a Task (`update_task`)**: Prompts for the task number to update, verifies bounds and format, and replaces the task description with the updated text.
4. **Remove a Task (`remove_task`)**: Prompts for the task number to remove, validates the selection, and deletes the task using Python's `.pop()` method.
5. **Interactive Menu & Error Handling**:
   - Re-displays the menu continuously using a `while` loop until the user selects Exit.
   - Gracefully catches non-numeric inputs using `try / except ValueError`.
   - Rejects out-of-bounds task numbers and displays clear error messages.
   - Rejects invalid menu options and re-displays the menu.

---

## 💡 Key Programming Concepts Demonstrated

- **Python Lists**: Using `.append()` to add items, list indexing `tasks[index]` for updates, and `.pop(index)` for deletion.
- **1-Based vs 0-Based Indexing**: Bridging user-friendly numbering (1, 2, 3...) to Python's internal zero-based indices (`task_num - 1`).
- **Looping & Flow Control**: A `while True` loop kept alive until broken by the exit condition.
- **Conditional Branching**: `if / elif / else` structures for menu routing and validation checks.
- **Exception Handling**: `try / except ValueError` to safely parse integers without crashing the program.
- **Modularity & Clean Code**: Breaking functionality into dedicated functions (`add_task`, `view_tasks`, `update_task`, `remove_task`, `main`) and passing the task list as a parameter.
- **Entry Point Idiom**: Using `if __name__ == "__main__":` to execute `main()` when run directly.

---

## 🚀 How to Run

### Prerequisites
- Python 3.6 or newer (no third-party packages required).

### Running the Application
Open a terminal in the project directory and run:

```bash
python todo.py
```

### Running the Automated Tests
A comprehensive test suite (`test_todo.py`) is included to verify all operations and edge cases:

```bash
python test_todo.py
```

---

## 🖥️ Sample Execution

```text
=============================
      TO-DO LIST MENU        
=============================
1. Add a task
2. View all tasks
3. Update a task
4. Remove a task
5. Exit
=============================
Enter your choice (1-5): 1

Enter the task description: Buy groceries
Success: Task 'Buy groceries' added successfully!

=============================
      TO-DO LIST MENU        
=============================
1. Add a task
2. View all tasks
3. Update a task
4. Remove a task
5. Exit
=============================
Enter your choice (1-5): 1

Enter the task description: Read Python documentation
Success: Task 'Read Python documentation' added successfully!

=============================
      TO-DO LIST MENU        
=============================
1. Add a task
2. View all tasks
3. Update a task
4. Remove a task
5. Exit
=============================
Enter your choice (1-5): 2

--- To-Do List ---
1. Buy groceries
2. Read Python documentation

=============================
      TO-DO LIST MENU        
=============================
1. Add a task
2. View all tasks
3. Update a task
4. Remove a task
5. Exit
=============================
Enter your choice (1-5): 3

--- To-Do List ---
1. Buy groceries
2. Read Python documentation

Enter the task number to update: 2
Enter the new task description: Read Python documentation for 30 minutes
Success: Task 2 updated from 'Read Python documentation' to 'Read Python documentation for 30 minutes'.

=============================
      TO-DO LIST MENU        
=============================
1. Add a task
2. View all tasks
3. Update a task
4. Remove a task
5. Exit
=============================
Enter your choice (1-5): 4

--- To-Do List ---
1. Buy groceries
2. Read Python documentation for 30 minutes

Enter the task number to remove: 1
Success: Task 'Buy groceries' removed successfully!

=============================
      TO-DO LIST MENU        
=============================
1. Add a task
2. View all tasks
3. Update a task
4. Remove a task
5. Exit
=============================
Enter your choice (1-5): 9
Error: Invalid menu choice. Please enter a number between 1 and 5.

=============================
      TO-DO LIST MENU        
=============================
1. Add a task
2. View all tasks
3. Update a task
4. Remove a task
5. Exit
=============================
Enter your choice (1-5): 5

Goodbye! Have a productive day.
```

For the complete terminal transcript, see [sample_output.txt](sample_output.txt).
