def selection_sort(items):

    if type(items) is list:
        n = len(items)
        for i in range(0, n):
            min_item = i

            for j in range(i+1, n):
                if items[j] < items[min_item]:
                    min_item = j
            print('min: ', items[min_item], ' -> ', items)
            if min_item != i:

                temp = items[i]

                items[i] = items[min_item]
                items[min_item] = temp


if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
    test = [11, 25, 12, 22, 64]
    print(' original  ', test)
    selection_sort(test)
    print(' sorted    ', test)
