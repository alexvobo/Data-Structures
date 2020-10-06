def merge_sort(items):

    if type(items) is list:
        n = len(items)
        if n <= 1:
            return items
        left = []
        right = []

        # Split the items list up into two separate lists, left and right
        for i, item in enumerate(items):
            if i < n/2:
                left.append(item)
            else:
                right.append(item)
        print('split: {} -> {} | {}'.format(items, left, right))

        # Recursively split the two lists further  until we cant split them any more
        left = merge_sort(left)
        right = merge_sort(right)

        # Merge the left/right lists
        return merge(left, right)


def merge(left, right):
    res = []
    leftCopy = left.copy()
    rightCopy = right.copy()
    # Merge the lists until they are in order, return the sorted merged list
    while left and right:
        if left[0] <= right[0]:
            res.append(left[0])
            left.pop(0)
        else:
            res.append(right[0])
            right.pop(0)
    while left:
        res.append(left[0])
        left.pop(0)
    while right:
        res.append(right[0])
        right.pop(0)
    print('merge: {} {} -> {}'.format(leftCopy, rightCopy, res))
    return res


if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

    print(' original  ', item_list)
    item_list = merge_sort(item_list)
    print(' sorted    ', item_list)
