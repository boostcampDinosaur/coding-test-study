from collections import deque
from itertools import permutations


def str2deque(expression: str) -> deque:
    # expression을 deque으로 변경해주기
    past = ""
    expression_deque = deque()
    for cur_char in expression[:-1]:
        if cur_char in ("*", "+", "-"):
            expression_deque.append(int(past))
            expression_deque.append(cur_char)
            past = ""
        else:
            past += cur_char
    # 마지막 문자 넣어서 덱에 추가
    past += expression[-1]
    expression_deque.append(int(past))

    return expression_deque


def calculate(n1: int, n2: int, ops: str) -> int:
    # eval은 위험하니까 함수 만들어보자.
    if ops == "+":
        return n1 + n2
    elif ops == "-":
        return n1 - n2
    elif ops == "*":
        return n1 * n2
    else:
        raise ValueError("+-* 말고 다른거 들어옴")


def calculate_one_operator_all(input_deque: deque, operator: str) -> deque:
    # *, +, - 이거 중에 하나 정해서 먼저 다 계산
    return_deque = deque()
    while input_deque:
        cur_exp = input_deque.popleft()
        if cur_exp != operator:
            return_deque.append(cur_exp)
        else:
            past_num = return_deque.pop()
            next_num = input_deque.popleft()
            cur_num = calculate(past_num, next_num, cur_exp)
            return_deque.append(cur_num)
    return return_deque


def solution_per_priority(expression_deque: deque, first: str, second: str, third: str):
    # *, -, + 의 우선순위가 정해진 경우 결과 계산

    # 순서대로 세개 모두 계산
    first_deque = calculate_one_operator_all(expression_deque, first)
    second_deque = calculate_one_operator_all(first_deque, second)
    third_deque = calculate_one_operator_all(second_deque, third)

    if len(third_deque) != 1:
        raise ValueError("왜 길이가 1이 아니지?")

    return abs(third_deque.pop())


def solution(expression):
    answer = 0
    expression_deque = str2deque(expression)
    operators = ("*", "+", "-")

    for first, second, third in permutations(operators):
        answer = max(
            answer, solution_per_priority(expression_deque.copy(), first, second, third)
        )

    return answer
