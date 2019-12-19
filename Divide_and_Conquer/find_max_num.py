import random


def generate_list(n):
    last_int = random.randint(1, 900)
    unimodal_list = [last_int]
    while len(unimodal_list) < n:
        step = random.randint(1, 900)
        last_int += step
        unimodal_list.append(last_int)

    max_element = unimodal_list[-1]
    unimodal_list.remove(max_element)
    break_point = random.randint(1, len(unimodal_list))
    left = unimodal_list[:break_point]
    right = unimodal_list[break_point:]
    left.append(max_element)
    unimodal_list = left + sorted(right, reverse=True)
    return unimodal_list


def find_maximum_element(unimodal_list):
    if len(unimodal_list) == 2:
        if unimodal_list[0] > unimodal_list[1]:
            max = unimodal_list[0]
        else:
            max = unimodal_list[1]
        return max
    if len(unimodal_list) == 1:
        return unimodal_list[0]

    n = len(unimodal_list) // 2
    left = unimodal_list[:n]
    right = unimodal_list[n:]
    left_max = find_maximum_element(left)
    right_max = find_maximum_element(right)
    if left_max > right_max:
        max = left_max
    else:
        max = right_max
    return max


def main():
    unimodal_list = generate_list(10 ** 6)
    print(find_maximum_element(unimodal_list))


if __name__ == '__main__':
    main()
