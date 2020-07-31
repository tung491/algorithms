def same_bsts(ns1, ns2):
    if len(ns1) != len(ns2):
        return False

    if len(ns1) == 0 and len(ns2) == 0:
        return True

    if ns1[0] != ns2[0]:
        return False

    left1 = get_smaller(ns1)
    left2 = get_smaller(ns2)
    right1 = get_bigger_or_equal(ns1)
    right2 = get_bigger_or_equal(ns2)
    return same_bsts(left1, left2) and same_bsts(right1, right2)


def get_smaller(ns):
    smaller = []
    for i in range(1, len(ns)):
        if ns[i] < ns[0]:
            smaller.append(ns[i])
    return smaller


def get_bigger_or_equal(ns):
    bigger = []
    for i in range(1, len(ns)):
        if ns[i] > ns[0]:
            bigger.append(ns[i])
    return bigger