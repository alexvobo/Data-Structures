''' Keep going through the items, swapping adjacent items if they are out of order'''

''' Algorithm needs 1 full pass with no swaps to be considered sorted'''


def bubble_sort(items):

    if type(items) is list:
        n = len(items)
        passes = 0
        while n > 0:
            new_n = 0
            for i in range(1, n):
                if items[i-1] > items[i]:
                    items[i-1], items[i] = items[i], items[i-1]
                    new_n = i
                    print('(i={}|n={}): {}   Swap   {} > {}'.format(i,
                                                                    n, items, items[i], items[i-1]))
                else:
                    print('(i={}|n={}): {}  [Keep]  {} <= {}'.format(i,
                                                                     n, items, items[i-1], items[i]))
            # set n as the last index that was found to be smaller than its predecessor
            n = new_n
            passes += 1
            print("Pass %d Complete" % passes)


if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
    item_list = [5, 1, 4, 2, 8]
    print(' original  ', item_list)
    bubble_sort(item_list)
