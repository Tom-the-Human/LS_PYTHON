"""
Write a simple linked list implementation. The linked list is a fundamental 
data structure in computer science, often used in the implementation of 
other data structures.

The simplest kind of linked list is a singly linked list. Each element in 
the list contains data and a "next" field pointing to the next element in the 
list of elements. This variant of linked lists is often used to represent 
sequences or push-down stacks (also called a LIFO stack; Last In, First Out).

Let's create a singly linked list whose elements may contain a range of data 
such as the numbers 1-10. Provide methods to reverse the linked list and 
convert a linked list to and from a list.

P
Input: SimpleLinkedList instance, with a range of data (such as numbers 1-10)
Output: reversed SimpleLinkedList object, convert to and from list
Explicit:
1 create a singly linked list whose elements may contain a range of data
2 provide a method to reverse the linked list
3 provide methods to convert a linked list to and from a list
Implicit:
1 also requires a custom Element class 
    (presumably to include the pointer to the next element)
2 other SimpleLinkedList methods will also be needed, such as 
    `is_empty()`, `peek()`, and `pop()` 
    - this last makes me think SimpleLinkedList should inherit from list
3 Element methods will be needed including `is_tail()`
4 a number of attributes will be required for both classes

E
There are a variety of tests, which cover everything described in the problem
statement and more. I think I'll end up writing to particular tests to finalize
my work on this problem. For now, let's collect needed attributes and methods
for each class.
SimpleLinkedList
    self.size
    self.head
    self.push(x)
    self.peek()
    self.to_list()
    from_list()
    self.is_empty()
    self.reverse()
    self.pop()
    self.tail # assumed, don't see it referenced in the tests
                # may not need (or want) it, considering LIFO structure
Element
    self.datum
    self.is_tail()
    self.next  # note that element2.next == element1, so refers to prev idx (LIFO)
            # also note that next can stack, as in lst.head.next.next.next.datum
            # so I assume it needs to be a property

H


D
SimpleLinkedList objects (inherit from list?)
Element objects (datum, next)
lists

A

C
"""
class Element:
    def __init__(self, datum, _next=None):
        self.datum = datum
        self._next = _next

    @property
    def next(self):
        return self._next

    def is_tail(self):
        return self.next is None

class SimpleLinkedList:
    def __init__(self):
        self.head = None

    @property
    def size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.next

        return size

    def push(self, datum):
        self.head = Element(datum, self.head)

    def peek(self):
        return self.head.datum if self.head else None
    
    def pop(self):
        if self.head is not None:
            popped = self.head
            self.head = self.head.next
            return popped.datum

    def to_list(self):
        list_out = []
        current = self.head
        while current is not None:
            list_out.append(current.datum)
            current = current.next

        return list_out

    @classmethod    
    def from_list(cls, lst):
        new_instance = cls()
        if not isinstance(lst, list):
            return new_instance

        copy = lst[:]
        copy.reverse()
        for ele in copy:
            new_instance.push(ele)

        return new_instance

    def reverse(self):
        reversed = self.__class__()
        current = self.head
        while current is not None:
            reversed.push(current.datum)
            current = current.next

        return reversed

    def is_empty(self):
        return self.head is None