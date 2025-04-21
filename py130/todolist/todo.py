class Todo:
    COMPLETE = 'x'
    INCOMPLETE = ' '
    def __init__(self, title):
        self.__title = title
        self._done = False

    @property
    def title(self):
        return self.__title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, status):
        if status is True or status is False:
            self._done = status
        else:
            print("Not a valid status, please only enter True or False!")

    def __str__(self):
        C = Todo.COMPLETE
        I = Todo.INCOMPLETE
        return f"[{C if self.done else I}] {self.title}"
    
    def __eq__(self, other):
        if isinstance(other, Todo):
            return (self.title, self.done) == (other.title, other.done)
        
        return NotImplemented
    
# tests

# def test_todo():
#     todo1 = Todo('Buy milk')
#     todo2 = Todo('Clean room')
#     todo3 = Todo('Go to gym')
#     todo4 = Todo('Clean room')

#     print(todo1)                  # [ ] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [ ] Clean room

#     print(todo2 == todo4)         # True
#     print(todo1 == todo2)         # False
#     print(todo4.done)             # False

#     todo1.done = True
#     todo4.done = True
#     print(todo4.done)             # True

#     print(todo1)                  # [X] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [X] Clean room

#     print(todo2 == todo4)         # False

#     todo4.done = False
#     print(todo4.done)             # False
#     print(todo4)                  # [ ] Clean room

# test_todo()