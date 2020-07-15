def max_subset_sum_no_adjancent(input_list: list) -> list:
    if not input_list:
        return
    elif len(input_list) == 1:
        return input_list[0]
    max_subset = input_list[:2]
    second = input_list[0]
    first = max(input_list[:2])
    for n in input_list[2:]: 
        curr_sum = max(first, second + n)
        first, second = curr_sum, first
        max_subset.append(curr_sum)
    return max_subset
    

if __name__ == "__main__":
    print(max_subset_sum_no_adjancent([7, 10, 12, 7, 9, 14]))
