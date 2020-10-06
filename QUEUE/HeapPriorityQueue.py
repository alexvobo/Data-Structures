import math


class MaxHeap:
    def __init__(self):
        self.pq = [""]
        self.size = 0

    def height(self):
        return math.floor(math.log(self.size))

    def maxPQ(self):
        return max(self.pq)

    def insert(self, v):
        self.pq.append(v)
        self.size += 1

        self.printpq()

    def delMax(self):
        max = self.pq[1]
        self.size -= 1
        self.exch(1, self.size)
        del self.pq[self.size+1]
        self.sink(1)
        print("removed: ", max)
        self.printpq()
        return max

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        print("swapped {} with {}".format(self.pq[j], self.pq[i]))
        self.printpq(print_size=False)

    def less(self, i, j):
        return bool((self.pq[i] > self.pq[j]) - (self.pq[i] < self.pq[j]))

    def swim(self, k):
        while (k > 1 and self.less(k/2, k)):
            self.exch(k/2, k)
            k = k/2

    def sink(self, k):
        while 2*k <= self.size:
            j = 2*k
            if (j < self.size and self.less(j, j+1)):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def printpq(self, print_size=True):
        if print_size:
            print(self.size, self.pq[1:])
        else:
            print(self.pq[1:])


if __name__ == "__main__":
    h = MaxHeap()
    h.insert("P")

    h.insert("Q")
    h.insert("E")

    h.delMax()
    h.insert("X")
    h.insert("A")
    h.insert("M")
    h.delMax()
    h.insert("P")
    h.insert("L")
    h.insert("E")
    h.delMax()
