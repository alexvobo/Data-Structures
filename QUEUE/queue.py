from LLIterator import LinkedListIterator
import random
EMPTY = "QUEUE IS EMPTY"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


''' Linked List version, stores nodes in First-In-First-Out (FIFO) order'''


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.first)

    ''' Add items to the rear of the queue'''

    def enqueue(self, item):
        if item:
            oldLast = self.last
            it = Node(item)
            self.last = it
            print("Enqueuing: ", it.data)
            if not self.first:
                self.first = self.last
            else:
                if oldLast:
                    oldLast.next = self.last
            self.size += 1

    ''' Remove items starting from the front'''

    def dequeue(self):
        if self.first:
            popped = self.first
            print("Dequeuing: ", popped.data)
            self.first = self.first.next
            self.size -= 1

            return popped
        else:
            print(EMPTY)


if __name__ == "__main__":
    queue = Queue()

    for _ in range(5):
        queue.enqueue(random.randint(0, 100))

    print("---")

    for _ in range(queue.size):
        queue.dequeue()
