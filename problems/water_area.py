def water_area(heights):
    maxes = [0 for _ in range(len(heights))]
    left_max = 0
    for i, height in enumerate(heights):
        maxes[i] = left_max
        left_max = max(left_max, height)
    right_max = 0
    for i in range(0, len(heights), -1):
        height = heights
       min_height = min(right_max, maxes[i])
       if height < min_height:
           maxes[i] = min_height - height
        else:
            maxes[i] = 0
        right_max = max(right_max, height)
    return sum(maxes)

        