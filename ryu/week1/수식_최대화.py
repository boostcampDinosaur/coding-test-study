from itertools import permutations
import re


def cal(num1, num2, op):
    if op == '-':
        return int(num1) - int(num2)
    if op == '+':
        return int(num1) + int(num2)
    if op == '*':
        return int(num1) * int(num2)


def solution(expression):
    answer = 0
    ops = re.findall("\D", expression)
    nums = re.findall("\d+", expression)

    for op in permutations(set(ops), len(set(ops))):  # set을 통해 중복 제거한 뒤 모든 우선순위 조합 경우의 수 반복
        temp_ops = ops[:]
        temp_nums = nums[:]
        for o in op:  # 연산자 우선순위 별로 출력
            while o in temp_ops:  # temp_ops에 연산자가 존재할 때까지 반복
                op_idx = temp_ops.index(o)  # 연산자의 인덱스 저장
                num1, num2, = int(temp_nums[op_idx]), int(temp_nums[op_idx + 1])  # 연산자의 인덱스 양 옆은 그 연산자를 수행하는 숫자들이니 불러옴
                result = cal(num1, num2, o)  # 연산 수행
                temp_ops.pop(op_idx)  # 연산자 pop
                del temp_nums[op_idx: op_idx + 2]  # 연산 수행한 두 숫자 삭제
                temp_nums.insert(op_idx, result)  # 연산 수행한 값을 연산자 인덱스에 삽입
        answer = max(answer, abs(temp_nums[0]))  # 최댓값 구함

    return answer