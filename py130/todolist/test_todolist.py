import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3], 
                         self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertEqual(self.todos.all_done(), False)

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add('not a todo')
        with self.assertRaises(TypeError):
            self.todos.add(1)
        with self.assertRaises(TypeError):
            self.todos.add(TodoList("Another To Do List"))

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        with self.assertRaises(IndexError):
            self.todos.todo_at(5)

    def test_mark_done_at(self):
        self.todos.mark_done_at(0)
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(5)

        self.assertTrue(self.todo1.done)
        self.assertFalse(self.todo2.done)

    def test_mark_undone_at(self):
        self.todos.mark_undone_at(0)
        self.todos.mark_done_at(1)
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(5)

        self.assertFalse(self.todo1.done)
        self.assertTrue(self.todo2.done)

    def test_mark_all_done(self):
        self.assertFalse(self.todos.all_done())
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())
        self.assertTrue(self.todo1.done)

    def test_remove_at(self):
        self.todos.remove_at(0)
        self.assertEqual(len(self.todos), 2)

        with self.assertRaises(IndexError):
            self.todos.remove_at(5)

    def test_str(self):
        string = (
        "----- Today's Todos -----\n"
        "[ ] Buy milk\n"
        "[ ] Clean room\n"
        "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):
        self.todos.mark_done('Buy milk')
        string = (
        "----- Today's Todos -----\n"
        "[x] Buy milk\n"
        "[ ] Clean room\n"
        "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_str_all_done_todos(self):
        self.todos.mark_all_done()
        string = (
        "----- Today's Todos -----\n"
        "[x] Buy milk\n"
        "[x] Clean room\n"
        "[x] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_each(self):
        list_test =[]
        self.todos.each(lambda todo: list_test.append(todo))
        self.assertEqual(list_test, [self.todo1, self.todo2, self.todo3])

    def test_select(self):
        self.todo1.done = True
        selection = self.todos.select(lambda todo: todo.done)
        self.assertEqual("----- Today's Todos -----\n[x] Buy milk",
                     str(selection))

if __name__ == "__main__":
    unittest.main()