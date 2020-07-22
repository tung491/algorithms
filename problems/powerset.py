def powerset(ns):
    subsets = [[]]
    for n in ns:
        for i in range(len(subsets)):
            curr_subset = subsets[i]
            subsets.append([*curr_subset, n])
    return subsets


def powerset1(ns, i=None):
    if i is None:
        i = len(ns) - 1
    elif i == -1:
        return [[]]
    n = ns[i]
    subsets = powerset1(ns, i - 1)
    subsets += [[*subset, n] for subset in subsets]
    return subsets


if __name__ == '__main__':
    print(powerset1([1, 2, 3]))
