"""
Unit and integration tests for todo.py.
Tests all operations and edge cases using unittest and mock inputs.
"""

import io
import unittest
from unittest.mock import patch
import todo


class TestTodoApp(unittest.TestCase):

    def test_view_tasks_empty(self):
        tasks = []
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            todo.view_tasks(tasks)
            output = fake_out.getvalue()
            self.assertIn("No tasks yet.", output)

    def test_add_task_success(self):
        tasks = []
        with patch("builtins.input", return_value="Write tests"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.add_task(tasks)
                self.assertEqual(tasks, ["Write tests"])
                self.assertIn("added successfully", fake_out.getvalue())

    def test_add_task_empty(self):
        tasks = []
        with patch("builtins.input", return_value="   "):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.add_task(tasks)
                self.assertEqual(tasks, [])
                self.assertIn("Error: Task description cannot be empty.", fake_out.getvalue())

    def test_view_tasks_numbered(self):
        tasks = ["Task One", "Task Two"]
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            todo.view_tasks(tasks)
            output = fake_out.getvalue()
            self.assertIn("1. Task One", output)
            self.assertIn("2. Task Two", output)

    def test_update_task_empty_list(self):
        tasks = []
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            todo.update_task(tasks)
            self.assertIn("No tasks yet.", fake_out.getvalue())

    def test_update_task_success(self):
        tasks = ["Old Task"]
        inputs = iter(["1", "New Updated Task"])
        with patch("builtins.input", side_effect=lambda *args: next(inputs)):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.update_task(tasks)
                self.assertEqual(tasks, ["New Updated Task"])
                self.assertIn("updated from 'Old Task' to 'New Updated Task'", fake_out.getvalue())

    def test_update_task_non_numeric(self):
        tasks = ["Keep Task"]
        with patch("builtins.input", return_value="abc"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.update_task(tasks)
                self.assertEqual(tasks, ["Keep Task"])
                self.assertIn("Please enter a valid numeric task number", fake_out.getvalue())

    def test_update_task_out_of_range(self):
        tasks = ["Keep Task"]
        with patch("builtins.input", return_value="5"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.update_task(tasks)
                self.assertEqual(tasks, ["Keep Task"])
                self.assertIn("Task number out of range", fake_out.getvalue())

    def test_update_task_empty_description(self):
        tasks = ["Keep Task"]
        inputs = iter(["1", "   "])
        with patch("builtins.input", side_effect=lambda *args: next(inputs)):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.update_task(tasks)
                self.assertEqual(tasks, ["Keep Task"])
                self.assertIn("Task description cannot be empty", fake_out.getvalue())

    def test_remove_task_empty_list(self):
        tasks = []
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            todo.remove_task(tasks)
            self.assertIn("No tasks yet.", fake_out.getvalue())

    def test_remove_task_success(self):
        tasks = ["First", "Second"]
        with patch("builtins.input", return_value="1"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.remove_task(tasks)
                self.assertEqual(tasks, ["Second"])
                self.assertIn("Task 'First' removed successfully!", fake_out.getvalue())

    def test_remove_task_non_numeric(self):
        tasks = ["First"]
        with patch("builtins.input", return_value="xyz"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.remove_task(tasks)
                self.assertEqual(tasks, ["First"])
                self.assertIn("Please enter a valid numeric task number", fake_out.getvalue())

    def test_remove_task_out_of_range(self):
        tasks = ["First"]
        with patch("builtins.input", return_value="0"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.remove_task(tasks)
                self.assertEqual(tasks, ["First"])
                self.assertIn("Task number out of range", fake_out.getvalue())

    def test_main_menu_flow(self):
        # Full workflow: view empty -> add -> view -> update -> remove -> invalid choice -> exit
        inputs = iter([
            "2",                      # View empty
            "1", "Clean workspace",   # Add task
            "2",                      # View tasks
            "3", "1", "Deep clean workspace",  # Update task
            "4", "1",                 # Remove task
            "99",                     # Invalid menu choice
            "5"                       # Exit
        ])
        with patch("builtins.input", side_effect=lambda *args: next(inputs)):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                todo.main()
                output = fake_out.getvalue()
                self.assertIn("No tasks yet.", output)
                self.assertIn("Task 'Clean workspace' added successfully!", output)
                self.assertIn("1. Clean workspace", output)
                self.assertIn("updated from 'Clean workspace' to 'Deep clean workspace'", output)
                self.assertIn("Task 'Deep clean workspace' removed successfully!", output)
                self.assertIn("Invalid menu choice", output)
                self.assertIn("Goodbye!", output)


if __name__ == "__main__":
    unittest.main()
