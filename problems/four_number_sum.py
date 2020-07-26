from collections import
def four_number_sum(ns, target_sum):
    all_pair_sum = {}
    quadruplets = []
    for i in range(1, len(ns) - 1):
        for j in range(i + 1, len(ns)):
            curr_sum = ns[i] + ns[j]
            diff = target_sum - curr_sum
            for diff in all_pair_sum:
                for pair in all_pair_sum[diff]:
                    quadruplets.append([*pair, ns[i], ns[j]])
        for k in range(0, i):
            curr_sum = ns[i] + ns[k]
            if curr_sum not in all_pair_sum:
                all_pair_sum[curr_sum] = [[ns[k], ns[i]]]
            else:
                all_pair_sum[curr_sum].append([ns[k], ns[i]])