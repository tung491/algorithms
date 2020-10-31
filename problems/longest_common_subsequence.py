# def longest_common_subsequence(str1, str2):
#     lcs = [[[] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             if str2[i - 1] == str1[j - 1]:
#                 lcs[i][j] = lcs[i - 1][j - 1].append(str2[i - 1])
#             else:
#                 lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)
#             return lcs[-1][-1]

def longest_common_subsequence(str1, str2):
    lcs = [[[None, 0, None, None] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = [str2[i - 1], lcs[i - 1][j -1][1] + 1, i - 1, j - 1]
            else:
                if lcs[i -1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]
        return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 or j != 0:
        current_entry = lcs[i][j]
        if current_entry[0]:
            sequence.append(current_entry[0])
        i = current_entry[2]
        j = current_entry[3]
    return list(reversed(sequence))
