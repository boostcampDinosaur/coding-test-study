from itertools import permutations


def split_calculate(expression_split, ops):
    exp = expression_split[:]  # expression_split 자체가 변하지 않도록 새로운 변수로 받음
    for op in ops:
        result = []
        while exp:  # 하나씩 빼서 result로 옮길 것임
            temp = exp.pop(0)  # 맨 앞의 것이
            if temp == op:  # 타겟으로 하는 연산자라면 아래 규칙에 따라 새로 pop 하여 result에 append
                if temp == "+":
                    result.append(result.pop() + exp.pop(0))
                elif temp == "-":
                    result.append(result.pop() - exp.pop(0))
                elif temp == "*":
                    result.append(result.pop() * exp.pop(0))
            else:  # 타켓으로 하는 연산자가 아니라면 그냥 result에 append
                result.append(temp)
        exp = result  # exp를 result로 업데이트 -> 현재 op 연산자는 제거된 상태일 것
    return abs(result[0])  # 결국 result에는 숫자 하나가 남을 것


def solution(expression):
    result = []
    expression_split = []  # expression을 split하여 숫자, 연산자만을 저장
    temp = 0
    for idx, exp in enumerate(expression):  # expression을 한 글자씩 탐색
        if exp in ["+", "-", "*"]:  # 해당 글자가 연산자 중 하나라면
            expression_split.append(
                int(expression[temp:idx])
            )  # 이전에 나온 숫자들을 하나의 정수로 append
            expression_split.append(exp)  # 해당 연산자를 append
            temp = idx + 1
        if idx == len(expression) - 1:  # 끝 숫자를 처리
            expression_split.append(int(expression[temp : idx + 1]))

    for ops in permutations(["+", "-", "*"], 3):  # 연산자 3개의 순열이 가능한 모든 경우의 수
        result.append(
            split_calculate(expression_split, ops)
        )  # expression에 애초에 없는 연산자라면 그냥 통과할테니 상관없음

    return max(result)


# 연산자는 총 3개, 최대 6개의 연산 순서 경우의 수
# bruteforce? 일단 숫자, 연산자를 다 끊고 리스트에 저장. 리스트에 들어있는 요소를 다 돈다. 최대 100자리 문자열이라서 다 돌아도 부담이 없다. + 가 나오면 앞 뒤 숫자를 합연산, - 가 나오면 ...
#    -> split으로 하려다가 이상한 곳으로 빠져버림.... split의 연속이다? 하지말자...
# 연산자다? 앞의 수와 뒤의 수를 연산... => 그럼 뒤에 것을 참조하는 꼴이어야 하나? 그럼 다음 글자일 때는 또 그걸 검사해?
# 겹치는 작동이 있으면 안됨... 가능은 하겠지만 비효율적임
# a 리스트, b 스택 -> a 앞의 것을 빼서 b에 넣음. a가 연산자라면 a를 하나 더 앞의 것 빼기, b를 팝해서 연산하여 b에 넣음
#    tip 이 방식 자체를 익혀두자. 스택과 팝을 사용해, 중복하여 참조하지 않는 유용한 방식

# 교훈
# 숫자를 대체하는 스킬 알아두자 -> del index , insert index
# pop(0) 말고 deque 쓰자
