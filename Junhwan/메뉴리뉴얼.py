from itertools import combinations
from collections import defaultdict


def results_per_n(orders, n):
    """
    n개의 메뉴 조합일 때 가장 많이 선택된 것 찾아보자.
    """
    counter = defaultdict(int)
    for order in orders:
        for comb_menu in combinations(order, n):
            comb_menu = "".join(sorted(comb_menu))
            counter[comb_menu] += 1

    max_value = max(counter.values()) if counter.values() else 0
    if max_value < 2:
        return []

    return [k for k, v in counter.items() if v == max_value]


def solution(orders, course):
    answer = []

    for n in course:
        answer.extend(results_per_n(orders, n))

    return sorted(answer)
