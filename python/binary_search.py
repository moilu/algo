list = []
list.extend(range(1, 21))


def binary_search(ordered_list, searched_value):
    low = 0
    high = len(ordered_list) - 1
    while low <= high:
        middle = int((low + high) / 2)

        if ordered_list[middle] == searched_value:
            return ordered_list[middle]
        if ordered_list[middle] > searched_value:
            high = middle - 1
        else:
            low = middle + 1
    return None


value = binary_search(list, 21)
print(value)
