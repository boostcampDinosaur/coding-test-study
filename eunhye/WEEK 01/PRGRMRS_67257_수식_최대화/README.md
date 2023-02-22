## 풀이

우선 `divide` 함수로 문자열 `expression`에서 숫자(`operands`)와 연산자(`operators`)를 구분해줍니다.

우선순위의 경우의 수는 `+, -, *` 모두 사용했을 시 `3!`로 6가지 조합이 최대이므로 모든 우선순위를 확인해주어도 무리는 없을 것이라 판단하였습니다. `permutations` 모듈을 사용하여 연산자의 우선순위 경우의 수를 다음과 같이 구해줍니다.

```python
operators = ["-", "*", "-", "+"]
permu = [p for p in permutations(set(operators))]
print(permu)
# [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
```

`permu`에서 `for`문을 통해 우선순위를 하나씩 꺼내어 해당 우선순위에 대한 계산을 해줍니다. 숫자는 항상 연산자보다 하나 더 많기 때문에 미리 `rands`에서 `popleft`한 첫 숫자를 `stack1`에 넣어줍니다. 그 다음 `rators`에서 연산자를 하나씩 돌아줍니다. 연산자 오른쪽에 오는 숫자를 먼저 `rands`에서 `popleft`하여 `stack1`에 넣어줍니다. 그 다음 가장 우선되는 연산자 `p_rator`와 현재 연산자 `curr`를 비교하여 같지 않다면 `curr`를 `stack2`에 저장해줍니다. `p_rator`와 `curr`가 같다면 `stack1`에서 미리 넣어 둔 마지막 두 숫자를 `pop`하여 연산을 진행하고 나온 숫자를 다시 `stack1`에 넣어줍니다. 이런 식으로 진행하게 된다면 끝에는 `p_rator` 연산을 하고 나온 숫자들은 모두 `stack1`에, 그리고 연산되지 않은 나머지 연산자들은 `stack2`에 저장이 되며 모든 연산자들을 다 연산해주기 위해 `rands`와 `rators`를 각각 `stack1`과 `stack2`로 업데이트해주고, `stack1`과 `stack2`는 다음 연산을 위해 비워줍니다.

하나의 우선순위 경우의 수를 확인해주고 나면 `rands`에는 숫자 하나만 남게 됩니다. 그 숫자와 현재 `answer`를 비교하여 큰 숫자로 `answer`를 업데이트 해주면 됩니다.

## 코드

```python
from itertools import permutations
from collections import deque

def divide(s):
    operator = "*+-"
    operands = []
    operators = []
    idx = -1

    for i in range(len(s)):
        if s[i] in operator:
            operands.append(int(s[idx+1:i]))
            operators.append(s[i])
            idx = i

    operands.append(int(s[idx+1:]))
    return operands, operators

def solution(expression):
    answer = 0
    operands, operators = divide(expression)
    permu = [p for p in permutations(set(operators))]

    for p in permu:
        stack1 = []
        stack2 = []
        rands = deque(operands)
        rators = deque(operators)
        for p_rator in p:
            stack1.append(rands.popleft())
            for curr in rators:
                stack1.append(rands.popleft())
                if curr != p_rator:
                    stack2.append(curr)
                    continue
                other_num = stack1.pop()
                new_num = stack1.pop()
                if p_rator == "*":
                    new_num *= other_num
                elif p_rator == "+":
                    new_num += other_num
                else:
                    new_num -= other_num
                stack1.append(new_num)

            rands = deque(stack1)
            rators = deque(stack2)
            stack1 = []
            stack2 = []
        answer = max(answer, abs(rands[0]))
    return answer
```
