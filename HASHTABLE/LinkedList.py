from LLIterator import LinkedListIterator

EMPTY = False
INDEX_OOB = "INDEX OUT OF BOUNDS"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def printList(self):
        ''' Prints the entire LinkedList in order'''
        if self.head:
            curr = self.head
            while curr is not None:
                print(curr.data)
                curr = curr.next
        else:
            print(EMPTY)

    def addFirst(self, item):
        ''' Add node to front of LinkedList'''
        if item:
            node = Node(item)
            if self.head:
                node.next = self.head
                self.head = node
            else:
                self.head = node
            self.size += 1

    def addLast(self, item):
        ''' Add node to the end of LinkedList'''
        if item:
            node = Node(item)
            if self.head:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = node
            else:
                self.head = node
            self.size += 1

    def add(self, item, index=None):
        ''' Index is specified => insert at the index.
            Index not specified => append to front of LinkedList
            Index of size-1 => append to rear of LinkedList '''
        if item:
            if index is None or index <= 0:
                self.addFirst(item)
            elif index >= self.getSize():
                self.addLast(item)
            else:
                node = Node(item)
                pos = 0
                curr = self.head
                ''' Look ahead by pre-incrementing position since we took care of index being 0 and index being out of bounds'''
                while curr.next is not None:
                    pos += 1

                    if pos == index:
                        node.next = curr.next
                        curr.next = node
                        self.size += 1
                        break

                    curr = curr.next

    def remove(self, index):
        ''' Removes node at specified index'''
        if self.head:
            if index is None or index >= self.getSize() or index < 0:
                return INDEX_OOB
            elif index == 0:
                return self.pop()
            else:
                future_pos = 1
                curr = self.head
                while curr is not None:
                    if future_pos == index:
                        removed_data = curr.next
                        if curr.next.next is not None:
                            ''' If there is a node after the node to be removed, skip over the removed node'''
                            curr.next = curr.next.next
                        else:
                            ''' If there is no node after the node to be removed, end the list at the current node'''
                            curr.next = None
                        self.size -= 1
                        return removed_data
                    future_pos += 1
                    curr = curr.next
        else:
            return EMPTY

    def get(self, index):
        ''' Gets the data of LinkedList item at specified index '''
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

    def getItem(self, item):
        ''' Gets the index of LinkedList item '''
        if self.head:
            if item:
                pos = 0
                curr = self.head

                while curr is not None:
                    if curr.data == item:
                        return pos, curr
                    pos += 1
                    curr = curr.next

        return EMPTY

    def peek(self):
        if self.head:
            return self.head
        else:
            return EMPTY

    def pop(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            self.size -= 1
            return popped
        else:
            return EMPTY

    def getSize(self):
        ''' Returns the amount of nodes in the LinkedList'''
        return self.size

    def reverseLL(self):
        first = self.head
        reverse = None

        while first is not None:
            second = first.next
            first.next = reverse
            reverse = first
            first = second

        self.head = reverse


if __name__ == "__main__":
    ll = LinkedList()

    ll.addFirst(5)
    ll.addLast(25)
    ll.add(123123123, -1)
    ll.add(1231231222223, 6)
    print('size', ll.getSize())
    #print('get', ll.get(None))

    ll.printList()
    print("iterating")
    myiter = iter(ll)
    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
    # print("Reversing")
    # ll.reverseLL()
    # ll.printList()
