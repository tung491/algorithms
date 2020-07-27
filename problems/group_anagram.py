from typing import List


def group_anagram(elements: List[str]) -> List[List[str]]:
    groups = {}
    for element in elements:
        sorted_order = ''.join(sorted(element))
        if sorted_order not in groups:
            groups[sorted_order] = [element]
        else:
            groups[sorted_order].append(element)
    return list(groups.values())


def test():
    print(group_anagram(['yo', 'oy', 'cat', 'tac', 'atc', 'flop', 'plof']))


if __name__ == '__main__':
    test()

