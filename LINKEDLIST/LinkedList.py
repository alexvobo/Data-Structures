from LLIterator import LinkedListIterator

EMPTY = "LinkedList Empty"
INDEX_OOB = "INDEX OUT OF BOUNDS"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def printList(l):
    ''' Prints the entire LinkedList in order'''
    if l:
        out = []
        curr = l

        while curr is not None:
            s = str(curr.data)+' ->' if curr.next else str(curr.data)
            out.append(s)
            curr = curr.next
        print(" ".join(out))
    else:
        print(EMPTY)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def print_list(self):
        ''' Prints the entire LinkedList in order'''
        if self.head:
            out = []
            curr = self.head

            while curr is not None:
                s = str(curr.data)+' ->' if curr.next else str(curr.data)
                out.append(s)
                curr = curr.next
            print(" ".join(out))
        else:
            print(EMPTY)

    def add_first(self, item=None):
        ''' Add node to front of LinkedList'''
        if item is not None:
            node = Node(item)
            if self.head:
                node.next = self.head
                self.head = node
            else:
                self.head = node
            self.size += 1

    def add_last(self, item=None):
        ''' Add node to the end of LinkedList'''
        if item is not None:
            node = Node(item)
            if self.head:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = node
            else:
                self.head = node
            self.size += 1

    def add(self, item=None, index=None):
        ''' Index is specified => insert at the index.
            Index not specified => append to front of LinkedList
            Index of size-1 => append to rear of LinkedList '''
        if item is not None:
            if index is None or index <= 0:
                self.add_first(item)
            elif index >= self.get_size():
                self.add_last(item)
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
            if index is None or index >= self.get_size() or index < 0:
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
            if index is None or index >= self.get_size() or index < 0:
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
            self.size -= 1
            return popped
        else:
            return EMPTY

    def get_size(self):
        ''' Returns the amount of nodes in the LinkedList'''
        return self.size

    def reverse_LL(self):
        first = self.head
        reverse = None

        while first is not None:
            second = first.next
            first.next = reverse
            reverse = first
            first = second

        self.head = reverse

    def insertion_sort(self):
        if self.head is not None and self.head.next is not None:
            new_list = None
            listptr = self.head
            print('\nSTART INSERTION SORT (new list forming)')

            while listptr is not None:
                curr = listptr
                listptr = listptr.next
                if new_list is None or curr.data < new_list.data:
                    curr.next = new_list
                    new_list = curr
                else:
                    ptr = new_list
                    while ptr is not None:
                        if ptr.next is None or (curr.data < ptr.next.data):
                            curr.next = ptr.next
                            ptr.next = curr
                            break
                        ptr = ptr.next
                printList(new_list)
            self.head = new_list
            print('END SORT\n')


if __name__ == "__main__":
    ll = LinkedList()

    nums = [3, 7, 4, 9, 5, 2, 6, 1]

    [ll.add_last(i) for i in nums]

    ll.print_list()
    ll.insertion_sort()
    ll.print_list()
    # print("iterating")
    # myiter = iter(ll)
    # print(next(myiter).data)
    # print(next(myiter).data)
    # print(next(myiter).data)
    # print(next(myiter).data)
    # print("Reversing")
    # ll.reverseLL()
    # ll.printList()
