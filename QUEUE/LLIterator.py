class LinkedListIterator:
    def __init__(self, first):
        self.curr = first

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curr:
            raise StopIteration
        else:
            node = self.curr
            self.curr = self.curr.next
            return node
