def get_permutation(ns):
    permutations = []
    permutation_helper(0, ns, permutations)
    return permutations


def permutation_helper(i, ns, permutations):
    def swap(i, j):
        ns[i], ns[j] = ns[j], ns[i]
   
    if i == len(ns) - 1:
        permutations.append(ns[:])
    else:
        for j in range(i, len(ns)):
            swap(i, j)
            permutation_helper(i + 1, ns, permutations)
            swap(j, i)


def test():
    print(get_permutation([1, 2, 3]))


if __name__ == '__main__':
    test()
