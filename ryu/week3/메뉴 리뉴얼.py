from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for course_num in course:  # 코스요리 개수
        orders_comb = []
        for order in orders:  # 주문 내역
            for comb in combinations(order, course_num):  # 코스요리에 맞는 개수만큼 조합 추출
                comb = ''.join(sorted(comb))  # 저장
                orders_comb.append(comb)

        orders_count = Counter(orders_comb).most_common()  # 가장 많은 순으로 뽑음

        for menu, cnt in orders_count:  # count가 1보다 크며, 가장 많은 애들만 answer에 추가
            if cnt == orders_count[0][1] and cnt > 1:
                answer.append(menu)
            else:
                break

    return sorted(answer)