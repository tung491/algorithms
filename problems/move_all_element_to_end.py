def move_elements_to_end(arr, to_move):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] == to_move and arr[j] == to_move:
            j -= 1
        elif arr[i] == to_move:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr
