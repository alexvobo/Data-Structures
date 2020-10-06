def quick_sort(items, lo=None, hi=None):
    if type(items) is list:

        if lo is None and hi is None:
            lo = 0
            hi = len(items)-1

        if lo < hi:
            part = partition(items, lo, hi)
            quick_sort(items, lo, part-1)
            quick_sort(items, part+1, hi)


def partition(items, lo, hi):
    pivot = items[hi]
    i = lo
    for j in range(lo, hi+1):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[hi] = items[hi], items[i]
    return i


if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

    print(' original  ', item_list)
    quick_sort(item_list)
    print(' sorted    ', item_list)
