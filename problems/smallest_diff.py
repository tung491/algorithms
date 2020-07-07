def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i1, i2 = 0, 0
    smallest = float('inf')
    current_diff = float('int')
    smallest_pair = []
    while i1 < len(arr1) and i2 < len(arr2):
        n1 = arr1[i1]
        n2 = arr2[i2]
        if n1 == n2:
            return [n1, n2]
        elif n1 < n2:
            current_diff = n2 - n1
            i1 += 1
        else:
            current_diff = n1 - n2
            i2 += 1
        if smallest > current_diff:
            smallest = current_diff
            smallest_pair = [n1, n2]
    return smallest_pair
