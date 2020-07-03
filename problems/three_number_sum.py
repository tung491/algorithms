def three_number_sum(input_list: list, target: int) -> list:
    triplets = []
    nums.sort()
    for i, n in enumerate(nums[:-2]):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = n + nums[left] + nums[right]
            if curr_sum == target:
                triplets.append([n, nums[left], nums[right]])
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return triplets


if __name__ == '__main__':
    print(three_number_sum([-8, -6, 1, 5, 3, 6, 8], 0))
