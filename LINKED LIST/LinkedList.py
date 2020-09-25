from LLIterator import LinkedListIterator

EMPTY = "LinkedList Empty"
INDEX_OOB = "INDEX OUT OF BOUNDS"


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

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

    def addFirst(self, node):
        ''' Add node to front of LinkedList'''
        if node:
            if self.head:
                node.next = self.head
                self.head = node
            else:
                self.head = node

    def addLast(self, node):
        ''' Add node to the end of LinkedList'''
        if node:
            if self.head:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = node
            else:
                self.head = node

    def add(self, node, index=None):
        ''' Index is specified => insert at the index.
            Index not specified => append to front of LinkedList
            Index of size-1 => append to rear of LinkedList '''
        if node:
            if index is None or index <= 0:
                self.addFirst(node)
            elif index >= self.getSize():
                self.addLast(node)
            else:
                pos = 0
                curr = self.head
                ''' Look ahead by pre-incrementing position since we took care of index being 0 and index being out of bounds'''
                while curr.next is not None:
                    pos += 1

                    if pos == index:
                        node.next = curr.next
                        curr.next = node
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

    def peek(self):
        if self.head:
            return self.head
        else:
            return EMPTY

    def pop(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            return popped
        else:
            return EMPTY

    def getSize(self):
        ''' Returns the amount of nodes in the LinkedList'''
        curr = self.head
        size = 0
        if curr:
            size = 1
            while curr.next is not None:
                size += 1
                curr = curr.next

        return size

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
    nodes = [Node(1), Node(2), Node(3), Node(4)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    ll.head = nodes[0]
    ll.addFirst(Node(5))
    ll.addLast(Node(25))
    ll.add(Node(123123123), -1)
    ll.add(Node(123123123), 6)
    print('size', ll.getSize())
    #print('get', ll.get(None))
    #print('removed', ll.remove(0))
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
