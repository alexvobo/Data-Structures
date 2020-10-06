
def bubble_sort(items):

    if type(items) is list:
        n = len(items)
        passes = 0
        while n > 0:
            newn = 0
            # i = iteration
            for i in range(1, n):
                if items[i-1] > items[i]:
                    items[i-1], items[i] = items[i], items[i-1]
                    newn = i
                    print('(i={}|n={}): {}   Swap   {} > {}'.format(i,
                                                                    n, items, items[i], items[i-1]))
                else:
                    print('(i={}|n={}): {}  [Keep]  {} <= {}'.format(i,
                                                                     n, items, items[i-1], items[i]))
            # set n as the last index that was found to be smaller than its predecessor
            n = newn
            passes += 1
            print("Pass %d Complete" % passes)


if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

    print(' original  ', item_list)
    bubble_sort(item_list)
