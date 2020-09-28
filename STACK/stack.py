from LLIterator import LinkedListIterator
import random

EMPTY = "QUEUE IS EMPTY"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


''' Linked List version, stores nodes in Last-In-First-Out (LIFO) order'''


class Stack:
    def __init__(self):
        self.first = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.first)

    ''' Put item on top of first item'''

    def push(self, item):
        oldFirst = self.first
        self.first = Node(item)
        print("Pushing: ", item)
        self.first.next = oldFirst
        self.size += 1
    ''' Removes first item '''

    def pop(self):
        if self.first:
            popped = self.first
            print("Popping: ", popped.data)
            self.first = self.first.next
            self.size -= 1
            return popped
        else:
            print(EMPTY)


if __name__ == "__main__":
    stack = Stack()

    for _ in range(5):
        stack.push(random.randint(0, 100))

    print("---")

    for _ in range(stack.size):
        stack.pop()
