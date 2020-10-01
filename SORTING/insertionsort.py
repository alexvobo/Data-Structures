def insertion_sort(items):

    if type(items) is list:
        for i in range(1, len(items)):
            current_item = items[i]
            prev_idx = i-1
            while prev_idx >= 0 and items[prev_idx] > current_item:
                items[prev_idx+1] = items[prev_idx]
                prev_idx -= 1
            items[prev_idx+1] = current_item
            i += 1

if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

    print(' original  ', item_list)
    insertion_sort(item_list)
    print(' sorted  ', item_list)
