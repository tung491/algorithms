import random


def generate_list(n):
    last_int = random.randint(1, 900)
    n_list = [last_int]
    while len(n_list) < n:
        step = random.randint(1, 900)
        last_int += step
        n_list.append(last_int)
    return n_list


def is_num_equal_index(n_list):
    if n_list[0] == 0:
        return True
    elif n_list[0] > 0:
        return False
    else:  # n_list[0] < 0
        if n_list[-1] == -1:
            return True
        elif n_list[-1] < -1:
            return False
        else:  # n_list[-1] > -1
            return divide_n_conquer(n_list)


def divide_n_conquer(n_list):
    n = len(n_list)
    median_index = (n // 2) - n
    if len(n_list) == 0:
        return False
    if n_list[median_index] == median_index:
        return True
    elif n_list[median_index] > median_index:
        left = n_list[:median_index]
        return divide_n_conquer(left)
    else:
        right = n_list[median_index:]
        return divide_n_conquer(right)


def main():
    n_list = generate_list(10 ** 6)
    print(is_num_equal_index(n_list))


if __name__ == '__main__':
    main()
