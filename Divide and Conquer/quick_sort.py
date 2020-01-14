count = 0


def is_median(ar, i, j, k):
    return (ar[j] > ar[i] > ar[k]) or (ar[j] < ar[i] < ar[k])


def quick_sort(a, left, right):
    global count
    if left >= right:
        return
    i = median_pivot(a, left, right)
    a[left], a[i] = a[i], a[left]
    count += right - left
    a, j = partition(a, left, right)
    quick_sort(a, left, j - 1)
    quick_sort(a, j + 1, right)


def partition(a, left, right):
    global count
    p = a[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[left], a[i - 1] = a[i - 1], a[left]
    return a, i - 1


def median_pivot(a, left, right):
    m = len(a) // 2 - 1
    if is_median(a, m, left, right):
        return m
    elif is_median(a, left, right, m):
        return left
    else:
        return right


def main():
    global count
    with open('input_w3.txt') as f:
        a = f.read().splitlines()
    a = list(map(int, a))
    quick_sort(a, 0, len(a) - 1)
    print(count)


if __name__ == "__main__":
    main()
