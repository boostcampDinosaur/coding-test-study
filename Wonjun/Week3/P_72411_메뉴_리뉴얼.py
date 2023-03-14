from itertools import combinations


def solution(orders, course):
    course_answer = []

    for course_nums in course:  # course대로 탐색
        course_temp = dict()  # course를 dict 형태로 저장할 것
        for order in orders:  # 주문을 하나씩 탐색하면서
            for comb in combinations(order, course_nums):  # 해당 주문 내의 조합을 탐색
                set_menu = "".join(sorted(list(comb)))  # 그것을 알파벳 정렬된 str로 변환
                if set_menu in course_temp:  # dict에 있으면 += 1 없으면 =1
                    course_temp[set_menu] += 1
                else:
                    course_temp[set_menu] = 1

        if not course_temp:  # 조합을 만들 수 없는 경우 continue
            continue

        max_course = max(course_temp.values())  # 여러 개일 수도 있기 때문에 최대 횟수를 취함

        if max_course == 1:  # 최대 횟수가 1인 경우 continue
            continue

        for cour in course_temp.items():
            if cour[1] == max_course:  # course 중에서 최대 횟수인 것을 정답으로 저장
                course_answer.append(cour[0])

    course_answer.sort()  # 알파벳 정렬
    return course_answer
