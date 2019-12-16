def brute_force_search(a):
    """
    Find the number inversion by using Brute Force Search
    :param a:
    :return: inversion_n: the number of inversions of a
    """
    inversion_n = 0
    n = len(a)
    for i in range(1, n - 1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                inversion_n += 1
    return inversion_n
    

def count_inv(a):
    """
    Find the inversion number of list a by using high-level Divide and Conquer algorithm
    :param a: input list
    :return: inversion_n: the number of inversions of a
    """
    n = len(a)
    if n in [0, 1]:
        inversion_n = 0
    else:
        first_half_a = a[:len(a) // 2]
        second_half_a = a[len(a) // 2:]
        left_inv = count_inv(first_half_a)
        right_inv = count_inv(second_half_a)
        split_inv = count_split_inv(a)
        inversion_n = left_inv + right_inv + split_inv
    return inversion_n


def sort_and_count_inv(a):
    """
    Sort the input list a and count the count the inversion of it
    :param a: input list (type: list)
    :return: b: sorted list of a (type: list),
             inversion_n: the number of inversion of a (type: int)
    """
    n = len(a)
    if n in [0, 1]:
        b = a
        inversion_n = 0
    else:
        first_half_a = a[:len(a) // 2]
        second_half_a = a[len(a) // 2:]
        c, left_inv =  sort_and_count_inv(first_half_a)
        d, right_inv = sort_and_count_inv(second_half_a)
        b, split_inv = merge_and_count_split_inv(c, d)
        inversion_n = left_inv + right_inv + split_inv
    return b, inversion_n


def merge_and_count_spilt_inv(c, d):
    """
    Merge and count the inversion number which is in both 2 halves
    Simplifying assumption: length of c (and d) * 2 = n is even
    :param c: input list(type: list)
           d: input list(type: list)
    :return: b: sorted list of a(type: list),
             inversion_n: the number of split inversions
    """
    n = len(c) * 2
    b = []
    i, j = 1, 1
    split_inv = 0
    for k in range(n):
        if c[i] > d[j]:
            b.append(c[i])
            i += 1
        else:
            b.append(d[j])
            j += 1
            split_inv += len(c) - i + 1
    return b, split_inv
