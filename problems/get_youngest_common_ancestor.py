def get_young_common_ancestor(top_ancestor, descendant_1, descendant_2):
    depth_1 = get_descendant_depth(descendant_1, top_ancestor)
    depth_2 = get_descendant_depth(descendant_2, top_ancestor)
    diff = abs(depth_2 - depth_1)
    if depth_1 > depth_2:
        return backtrack_ancestor_tree(descendant_1, descendant_2, diff)
    else:
        return backtrack_ancestor_tree(descendant_2, descendant_1, diff)


def get_descendant_depth(descendant, top_ancestor):
    depth = 0
    while descendant != top_ancestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrack_ancestor_tree(lower_descendant, higher_descendant, diff):
    while diff > 0:
        lower_descendant = lower_descendant.ancestor
        diff -= 1
    while lower_descendant != higher_descendant:
        lower_descendant = lower_descendant.ancestor
        higher_descendant = higher_descendant.ancestor
    return lower_descendant
