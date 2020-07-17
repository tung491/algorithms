def levenshtein_distance1(str1, str2):
    """
    Time: O(NM)
    Space: O(NM)
    :param str1:
    :param str2:
    :return:
    """
    edits = [[x for x in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        edits[i][0] = i
    for i2, c2 in enumerate(str2, start=1):
        for i1, c1 in enumerate(str1, start=1):
            if c2 == c1:
                edits[i2][i1] = edits[i2 - 1][i1 - 1]
            else:
                edits[i2][i1] = 1 + min(edits[i2 - 1][i1 - 1],
                                        edits[i2][i1 - 1],
                                        edits[i2 - 1][i1])
    return edits[-1][-1]


def levenshtein_distance2(str1, str2):
    if len(str1) < len(str2):
        short_str = str1
        long_str = str2
    else:
        short_str = str2
        long_str = str1
    even_edits = [i for i in range(len(short_str) + 1)]
    odd_edits = [None for _ in range(len(short_str) + 1)]
    for i, c1 in enumerate(long_str, start=1):
        if i % 2 == 1:
            current_edits = odd_edits
            previous_edits = even_edits
        else:
            current_edits = even_edits
            previous_edits = odd_edits
        current_edits[0] = i
        for j, c2 in enumerate(short_str, start=1):
            if c1 == c2:
                current_edits[j] = previous_edits[j - 1]
            else:
                current_edits[j] = 1 + min(previous_edits[j - 1],
                                           previous_edits[j],
                                           current_edits[j - 1])
    return even_edits[-1] if len(long_str) % 2 == 0 else odd_edits[-1]


if __name__ == '__main__':
    str1 = 'abc'
    str2 = 'yabd'
    print(levenshtein_distance2(str1, str2))
