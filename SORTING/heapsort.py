
def heap_sort(items):

    if type(items) is list:
        n = len(items)

        for i in range(n//2-1, -1, -1):
            heapify(items, n, i)

        for i in range(n-1, 0, -1):
            items[0], items[i] = items[i], items[0]
            heapify(items, i, 0)


def heapify(items, n, i):
    left = 2*i+1
    right = left+1
    maximum = i

    if left < n and items[left] > items[maximum]:
        maximum = left
        
    if right < n and items[right] > items[maximum]:
        maximum = right

    if maximum != i:
        items[i], items[maximum] = items[maximum], items[i]
        heapify(items, n, maximum)


if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

    print(' original  ', item_list)
    heap_sort(item_list)

    print(' sorted  ', item_list)
