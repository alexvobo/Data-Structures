from LLIterator import LinkedListIterator

EMPTY = "CircularLinkedList Empty"
INDEX_OOB = "INDEX OUT OF BOUNDS"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = self


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def printList(self):
        ''' Prints the entire CircularLinkedList in order'''
        if self.head:
            curr = self.head
            print(curr.data)
            while curr.next is not self.head:
                curr = curr.next
                print(curr.data)
        else:
            print(EMPTY)

    def addFirst(self, item):
        ''' Add node to front of CircularLinkedList'''
        if item:
            node = Node(item)
            if self.head:
                headptr = self.head
                curr = self.head
                node.next = self.head
                while curr.next != headptr:
                    curr = curr.next
                curr.next = node

                self.head = node
            else:
                self.head = node
            self.size += 1

    def addLast(self, item):
        ''' Add node to the end of CircularLinkedList'''
        if item:
            node = Node(item)
            if self.head:
                headptr = self.head
                curr = self.head
                while curr.next != headptr:
                    curr = curr.next
                node.next = self.head
                curr.next = node
            else:
                self.head = node
            self.size += 1

    def add(self, item, index=None):
        ''' Index is specified => insert at the index.
            Index not specified => append to front of CircularLinkedList
            Index of size-1 => append to rear of CircularLinkedList '''
        if item:
            if index is None or index <= 0:
                self.addFirst(item)
            elif index >= self.getSize():
                self.addLast(item)
            else:
                node = Node(item)
                pos = 0
                headptr = self.head
                curr = self.head
                ''' Look ahead by pre-incrementing position since we took care of index being 0 and index being out of bounds'''
                while curr.next != headptr:
                    pos += 1

                    if pos == index:
                        node.next = curr.next
                        curr.next = node
                        break

                    curr = curr.next
            self.size += 1

    def remove(self, index):
        ''' Removes node at specified index'''
        if self.head:
            if index is None or index >= self.getSize() or index < 0:
                return INDEX_OOB
            elif index == 0:
                return self.pop()
            else:
                future_pos = 1
                headptr = self.head

                curr = self.head
                while curr.next != headptr:
                    if future_pos == index:

                        removed_data = curr.next
                        curr.next = curr.next.next
                        self.size -= 1
                        return removed_data
                    future_pos += 1
                    curr = curr.next

        else:
            return EMPTY

    def get(self, index):
        ''' Gets the data of CircularLinkedList item at specified index '''
        if self.head:
            if index is None or index >= self.getSize() or index < 0:
                return INDEX_OOB
            else:
                pos = 0
                curr = self.head

                while pos != index:
                    pos += 1
                    curr = curr.next

                return curr
        else:
            return EMPTY

    def peek(self):
        if self.head:
            return self.head
        else:
            return EMPTY

    def pop(self):
        if self.head:
            popped = self.head

            if self.getSize() == 1:
                self.head = None
            else:
                headptr = self.head
                self.head = self.head.next

                curr = self.head
                while curr.next != headptr:
                    curr = curr.next
                curr.next = self.head
            self.size -= 1
            return popped
        else:
            return EMPTY

    def getSize(self):
        ''' Returns the amount of nodes in the CircularLinkedList'''
        return self.size


if __name__ == "__main__":
    ll = CircularLinkedList()
    ll.addFirst(5)
    ll.addFirst(2)
    ll.addFirst(1239292)
    # ll.addLast(Node(25))
    # ll.addLast(Node(9))
    ll.add(123, 1)
    # ll.add(Node(123123123), -1)
    ll.printList()
    print('size', ll.getSize())
    print('get', ll.get(3).next.data)
    print('removed', ll.remove(2).data)
    print('size', ll.getSize())

    print("Iterating")
    myiter = iter(ll)

    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
