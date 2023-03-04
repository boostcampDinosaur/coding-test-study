## 풀이

DFS로 풀어주었습니다.

고려해주어야 할 경우의 수는 세 가지입니다. 10으로 나누었을 때 나머지가

- 5보다 클 때는 더해주어야 합니다.
- 5보다 작을 때는 빼주어야 합니다.
- 5일 때는 더할 때와 뺄 때 둘다 고려해주어야 합니다.

`num`을 10으로 나눈 값으로 업데이트를 하며 `cnt`를 세어주고, `num`이 0일 때 `answer`를 `cnt`와 비교하여 업데이트 해주면 됩니다.

## 코드

```python
def dfs(cnt, num):
    global answer
    if num == 0:
        answer = min(cnt, answer)
        return
    dist = num % 10
    if dist == 5:
        dfs(cnt + (10 - dist), (num + (10 - dist)) // 10)
        dfs(cnt + dist, (num - dist) // 10)
    elif dist > 5:
        dfs(cnt + (10 - dist), (num + (10 - dist)) // 10)
    else:
        dfs(cnt + dist, (num - dist) // 10)


def solution(storey):
    global answer
    answer = float("inf")
    dfs(0, storey)
    return answer
```
