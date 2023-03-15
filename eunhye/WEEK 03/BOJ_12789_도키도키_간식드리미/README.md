## 풀이

queue와 stack을 이용하여 풀어주었습니다.

주어진 input list는 deque로 만들어주었고 빈 list인 stack도 만들어주었습니다.

1부터 N까지 돌아주며 break를 거치지 않고 for문을 잘 돌았다면 "Nice"를 출력해주었습니다.

queue의 첫 번째 원소가 order와 일치하다면 queue에서 popleft를 해주었습니다.
그렇지 않고, stack의 마지막 원소가 order와 일치하다면 stack에서 pop해주었습니다.
둘 다 해당하지 않을 때는 queue에서 order를 찾을 때까지 popleft를 해주어 stack에 append해주었습니다.

order와 일치하는 원소를 찾지 못하고 남은 queue 원소를 모두 stack에 넣어주고 끝이 났다면,
현재 찾아주려하는 order가 이미 stack에 들어가 있을 경우이며,
stack의 마지막 원소가 아닐 경우이기 때문에 불가능한 순서가 되므로 "Sad"를 출력해줍니다.

## 코드

```python
from collections import deque

N = int(input())
queue = deque(map(int, input().split()))
stack = []

for order in range(1, N + 1):
    if queue and queue[0] == order:
        queue.popleft()
    elif stack and stack[-1] == order:
        stack.pop()
    else:
        while queue:
            if queue[0] == order:
                queue.popleft()
                break
            stack.append(queue.popleft())
        else:
            print("Sad")
            break
else:
    print("Nice")
```
