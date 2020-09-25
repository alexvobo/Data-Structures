from LLIterator import LinkedListIterator

EMPTY = "DoublyLinkedList Empty"
INDEX_OOB = "INDEX OUT OF BOUNDS"


class Node:
    def __init__(self, data=None):
        self.data = data

        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def printList(self):
        ''' Prints the entire DoublyLinkedList in order'''
        if self.head:
            curr = self.head
            while curr is not None:
                print(curr.data)
                curr = curr.next
        else:
            print(EMPTY)

    def addFirst(self, item):
        ''' Add node to front of DoublyLinkedList'''
        if item:
            node = Node(item)
            if self.head:
                node.next = self.head
                self.head.prev = node

                self.head = node
            else:
                self.head = node
            self.size += 1

    def addLast(self, item):
        ''' Add node to the end of DoublyLinkedList'''
        if item:
            node = Node(item)
            if self.head:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                node.prev = curr
                curr.next = node
            else:
                self.head = node
            self.size += 1

    def add(self, item, index=None):
        ''' Index is specified => insert at the index.
            Index not specified => append to front of DoublyLinkedList
            Index of size-1 => append to rear of DoublyLinkedList '''
        if item:
            if index is None or index <= 0:
                self.addFirst(item)
            elif index >= self.getSize():
                self.addLast(item)
            else:
                node = Node(item)
                pos = 0
                beforeNode = self.head
                ''' Look ahead by pre-incrementing position since we took care of index being 0 and index being out of bounds'''
                while beforeNode.next is not None:
                    pos += 1

                    if pos == index:
                        node.next = beforeNode.next
                        node.prev = beforeNode
                        beforeNode.next.prev = node
                        beforeNode.next = node
                        self.size += 1
                        break

                    beforeNode = beforeNode.next

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
                            curr.next.next.prev = curr
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
        ''' Gets the data of DoublyLinkedList item at specified index '''
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
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return popped
        else:
            return EMPTY

    def getSize(self):
        ''' Returns the amount of nodes in the DoublyLinkedList'''
        return self.size


if __name__ == "__main__":
    ll = DoublyLinkedList()

    ll.addFirst(5)
    ll.addLast(25)
    ll.add(123123123123, 2)
    ll.add(82367, 3)
    i = 0
    #
    ll.add(99, i)
    print('size', ll.getSize())
    ll.printList()
    print('remove', ll.remove(i).data)
    print('size', ll.getSize())
    i = 1
    print('get i=%d ' % i,  ll.get(i).prev.data)
    print("iterating")
    myiter = iter(ll)

    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
    print(next(myiter).data)
