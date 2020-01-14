import random


def random_select(a, i):
    n = len(a)
    if n == 1:
        return a[0]
    try:
        p = random.randint(1, len(a))
    except:
        p = 0
    a, j = partition(a, p)
    if i == j + 1:
        return p
    elif j > i:
        return random_select(a[:p], i)
    else:
        return random_select(a[p + 1:], i - j)


def partition(a, p):
    left = 0
    right = len(a) - 1
    i = left + 1
    for j in range(left + 1, right + 1):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[left], a[i - 1] = a[i - 1], a[left]
    return a, i - 1


def main():
    test_case = [1, 5, 6, 2, 4, 12, 3]
    print(random_select(test_case, 2))


if __name__ == '__main__':
    main()
