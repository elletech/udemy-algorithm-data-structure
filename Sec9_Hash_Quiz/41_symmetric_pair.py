"""
Symmetric(左右対称)
Input   [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output  [(5, 3), (7,4)]
"""

from typing import List


def symmetric_pair(lists: List) -> List:
    pair_dict = dict()
    result_array = []
    for list_element in lists:
        if list_element[1] in pair_dict.keys():
            if list_element[0] in pair_dict.values():
                result_array.append(list_element)

        pair_dict[list_element[0]] = list_element[1]
    return result_array


if __name__ == '__main__':
    li = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(symmetric_pair(li))
