def longest_peak(arr):
    longest_peak_len = 0
    i = 1
    while i < len(arr) - 1:
        is_peak = max(arr[i], arr[i - 1], arr[i + 1]) == arr[i]
        if not is_peak:
            i += 1
            continue

        left_i = i - 2
        while left_i >= 0 and arr[left_i] < arr[left_i + 1]:
            left_i -= 1
        right_i = i + 2
        while right_i < len(arr) and arr[right_i] < arr[right_i - 1]:
            right_i += 1
        
        curr_peak_len = right_i - left_i - 1
        longest_peak_len = max(longest_peak_len, curr_peak_len)
        i = right_i
    return longest_peak_len
