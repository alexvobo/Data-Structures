
EMPTY = "DoublyLinkedList Empty"
INDEX_OOB = "INDEX OUT OF BOUNDS"


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        if next:
            next.prev = self
            self.next = next
        else:
            self.next = None

        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        ''' Prints the entire DoublyLinkedList in order'''
        if self.head:
            curr = self.head
            while curr is not None:
                print(curr.data)
                curr = curr.next
        else:
            print(EMPTY)

    def addFirst(self, node):
        ''' Add node to front of DoublyLinkedList'''
        if node:
            if self.head:
                node.next = self.head
                self.head.prev = node

                self.head = node
            else:
                self.head = node

    def addLast(self, node):
        ''' Add node to the end of DoublyLinkedList'''
        if node:
            if self.head:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                node.prev = curr
                curr.next = node
            else:
                self.head = node

    def add(self, node, index=None):
        ''' Index is specified => insert at the index.
            Index not specified => append to front of DoublyLinkedList
            Index of size-1 => append to rear of DoublyLinkedList '''
        if node:
            if index is None or index <= 0:
                self.addFirst(node)
            elif index >= self.getSize():
                self.addLast(node)
            else:
                pos = 0
                beforeNode = self.head
                ''' Look ahead by pre-incrementing position since we took care of index being 0 and index being out of bounds'''
                while beforeNode.next is not None:
                    pos += 1

                    if pos == index:
                        afterNode = beforeNode.next
                        beforeNode.next = node
                        node.prev = beforeNode
                        afterNode.prev = node
                        node.next = afterNode
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
            return popped
        else:
            return EMPTY

    def getSize(self):
        ''' Returns the amount of nodes in the DoublyLinkedList'''
        curr = self.head
        size = 0
        if curr:
            size = 1
            while curr.next is not None:
                size += 1
                curr = curr.next

        return size


if __name__ == "__main__":
    ll = DoublyLinkedList()

    ll.head = Node(1)
    ll.addFirst(Node(5))
    ll.addLast(Node(25))
    ll.add(Node(123123123), 2)
    ll.add(Node(823629), 3)
    i = 0
    print('remove', ll.remove(i).data)
    ll.add(Node(99), i)
    print('size', ll.getSize())
    ll.printList()
    i = 1
    print('get i=%d ' % i,  ll.get(i).next.data)
