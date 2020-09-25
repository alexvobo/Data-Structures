from LLIterator import LinkedListIterator


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


''' Linked List version, stores nodes in FIFO order'''


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.last)

    def isEmpty(self):
        return self.last == None

    def size(self):
        return self.size

    def push(self, item):
        oldFirst = self.last
        self.last = Node(item)
        self.last.next = oldFirst
        self.size += 1

    def pop(self):
        popped = self.last
        self.last = self.last.next
        self.size -= 1
        return popped


if __name__ == "__main__":
    queue = Queue()
    queue.push(4)
    queue.push(4)
    queue.pop()
    it = iter(queue)
    print(next(it).data)
