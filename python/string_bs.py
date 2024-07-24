# Lista de cadenas ordenadas alfabéticamente
ordered_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango',
                'orange', 'peach', 'pear', 'plum', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']


def binary_search(ordered_list, searched_value):
    low = 0
    high = len(ordered_list) - 1
    step = 0
    while low <= high:
        middle = int((low + high) / 2)

        if ordered_list[middle] == searched_value:
            step += 1
            print('This is BS step count: ' + str(step))
            return 'BS result: ' + ordered_list[middle]
        elif ordered_list[middle] > searched_value:
            step += 1
            high = middle - 1
        else:
            step += 1
            low = middle + 1
    print('This is BS step count: ' + str(step))
    return None


# Ejemplo de uso
searched_value = 'kiwi'
result = binary_search(ordered_list, searched_value)
print(result)
