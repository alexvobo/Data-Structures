from LLIterator import LinkedListIterator


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


''' Linked List version, stores nodes in LIFO order'''


class Stack:
    def __init__(self):
        self.first = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.first)

    def isEmpty(self):
        return self.first == None

    def size(self):
        return self.size

    def push(self, item):
        oldFirst = self.first
        self.first = Node(item)
        self.first.next = oldFirst
        self.size += 1

    def pop(self):
        popped = self.first
        self.first = self.first.next
        self.size -= 1
        return popped


if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(4)
    print('popped',stack.pop().data)
    it = iter(stack)
    print(next(it).data)
