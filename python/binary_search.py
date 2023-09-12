list = []
list.extend(range(1, 21))


def binary_search(ordered_list, searched_value):
    low = 0
    high = len(ordered_list) - 1
    while low <= high:
        middle = (low + high)
        guess = ordered_list[middle]
        if guess == searched_value:
            return guess
        if guess > searched_value:
            high = middle - 1
        else:
            low = middle + 1
    return None


value = binary_search(list, 23)
print(value)
