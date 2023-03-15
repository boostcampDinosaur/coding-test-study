from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        cnt = Counter()
        for order in orders:
            subset = set(["".join(sorted(combi)) for combi in combinations(order, c)])
            cnt.update(subset)
        most_common = cnt.most_common()
        for menu, num in most_common:
            _, most_picked = most_common[0]
            if num == most_picked and num >= 2:
                answer.append(menu)
    answer.sort()
    return answer
