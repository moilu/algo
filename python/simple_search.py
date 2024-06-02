def simple_search(ordered_list, searched_value):
    step = 0
    for num in ordered_list:
        if num == searched_value:
            step += 1
            print('This is SS step count: ' + str(step))
            return 'SS result: ' + str(num)
        else:
            step += 1
    print('This is SS step count: ' + str(step))
    return None
