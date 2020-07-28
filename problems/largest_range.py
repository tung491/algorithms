def largest_range(ns):
    best_range = []
    longest_range = 0
    nums = {}
    for n in ns:
        nums[n] = True
    for n in ns:
        if not nums[n]:
            continue
        nums[n] = False
        curr_len = 1
        left = n - 1
        right = n + 1
        while left in nums:
            nums[left] = False
            curr_len += 1
            left -= 1
        while right in nums:
            nums[right] = False
            curr_len += 1
            right += 1
        if curr_len > longest_range:
            longest_range = curr_len
            best_range = [left + 1, right - 1]
    return best_range
