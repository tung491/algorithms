import math


def max_area(height):
    max_ns = [(0, height[0]), (1, height[1])]
    maxarea = min(height[:2])
    for i, n in enumerate(height[2:], start=2):
        area1 = (i - max_ns[0][0]) * min(n, max_ns[0][1])
        area2 = (i - max_ns[1][0]) * min(n, max_ns[1][1])
        if area1 > maxarea and area1 > area2:
            maxarea = area1
            max_ns[1] = (i, n)
        elif area2 > maxarea:
            maxarea = area2
            max_ns = [max_ns[1], (i, n)]
    return maxarea


print(max_area([2, 3, 10, 5, 7, 8, 9]))
