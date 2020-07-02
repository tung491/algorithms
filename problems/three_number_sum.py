def three_number_sum(input_list: list, target: int) -> list:
    triplets = []
    input_list.sort()
    for i, n in enumerate(input_list[:-2]):
        left = i + 1
        right = len(input_list) - 1
        while left < right:
            curr_sum = n + input_list[left] + input_list[right]
            if curr_sum == target:
                triplets.append([n, input_list[left], input_list[right]])
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return triplets


if __name__ == '__main__':
    print(three_number_sum([-8, -6, 1, 5, 3, 6, 8], 0))
