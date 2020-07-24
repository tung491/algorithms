def longest_palindromic_substring(string):
    curr_longest = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_palindorm_from(string, i - 1, i + 1)
        even = get_longest_palindorm_from(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        curr_longest = max(longest, curr_longest, key=lambda x: x[1] - x[0])
    return string[curr_longest[0]: curr_longest[1]]


def get_longest_palindorm_from(string, left_i, right_i):
    while left_i >= 0 and right_i < len(string):
        if string[left_i] != string[right_i]:
            break
        left_i -= 1
        right_i += 1
    return [left_i + 1, right_i]


def test():
    print(longest_palindromic_substring('abaxyzzyxb'))


if __name__ == '__main__':
    test()

