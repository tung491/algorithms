import random


def comprasion(n_list, count):
    n = len(n_list)
    if n == 1:
        largest = n_list[0]
        second = 0
        return largest, second, count
    if n == 2:
        if n_list[0] > n_list[1]:
            count += 1
            largest, second = n_list[0], n_list[1]
        else:
            largest, second = n_list[1], n_list[0]
        return largest, second, count

    left = n_list[:n//2]
    right = n_list[n//2:]
    l1, l2, count = comprasion(left, count)
    r1, r2, count = comprasion(right, count)
    if l1 > r1:
        largest = l1
        count += 1
        if r1 > l2:
            second = r1
            count += 1
        elif l2 > l1:
            second = l2
            count += 1
        else:
            second = r2
    else:
        largest = r1
        if l1 > r2:
            count += 1
            second = l1
        elif r2 > l2:
            count += 1
            second = r2
        else:
            second = l2
    return largest, second, count


def main():
    n_list = [i ** 2 for i in range(5)]
    count = 0
    random.shuffle(n_list)
    largest, second, count = comprasion(n_list, count)
    print(f'The second largest in the list is {second} \n'
          f'The comparsion number is {count}')


if __name__ == '__main__':
    main()