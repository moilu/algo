list = list(range(1, 101))


def binary_search(ordered_list, searched_value):
    low = 0
    high = len(ordered_list) - 1
    step = 0
    while low <= high:
        middle = int((low + high) / 2)

        if ordered_list[middle] == searched_value:
            step += 1
            print('This is BS step number: ' + str(step))
            return 'BS result: ' + str(ordered_list[middle])
        elif ordered_list[middle] > searched_value:
            step += 1
            print('This is BS step number: ' + str(step))
            high = middle - 1
        else:
            step += 1
            print('This is BS step number: ' + str(step))
            low = middle + 1
    return None


def simple_search(ordered_list, searched_value):
    step = 0
    for num in ordered_list:
        if num == searched_value:
            step += 1
            print('This is SS step number: ' + str(step))
            return 'SS result: ' + str(num)
        else:
            step += 1
            print('This is SS step count: ' + str(step))


result_bs = binary_search(list, 87)
result_ss = simple_search(list, 87)
print(result_bs)
print(result_ss)
