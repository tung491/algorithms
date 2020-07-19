def longest_peak(arr):
    longest_peak_len = 0
    i = 1
    left_i = 0
    while i < len(arr) - 1:
        is_peak = arr[i] > arr[i - 1] and arr[i] > arr[i + 1]
        if not is_peak:
            if arr[i] <= arr[i - 1]:
                left_i = i
            i += 1
            continue

        right_i = i + 2
        while right_i < len(arr) and arr[right_i] < arr[right_i - 1]:
            right_i += 1
        
        curr_peak_len = right_i - left_i
        longest_peak_len = max(longest_peak_len, curr_peak_len)
        i = right_i - 1
    return longest_peak_len


if __name__ == "__main__":
    print(longest_peak([1, 2, 3, 3, 4, 0, 10,
                        6, 5, -1, -3, 2, 3]))
