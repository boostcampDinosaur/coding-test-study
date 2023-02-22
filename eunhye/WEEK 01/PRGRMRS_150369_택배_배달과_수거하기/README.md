## 풀이

그리디로 풀어주었습니다. 가장 멀리 있는 집부터 체크해주었습니다.

`deliver`와 `pickup`에 해당 집에 배달해야할 택배와 수거해야할 상자의 개수를 빼줍니다. 그 다음 `while`문을 돌아줄 때 `deliver`와 `pickup`을 `cap`으로 더해주며 해당 집에 몇 번을 방문해야 배달과 수거를 모두 끝낼 수 있을지 찾아줍니다. 그 후 해당 집을 몇 번 방문해야하는 지를 담은 `cnt`와 왕복이기 때문에 `2`를 거리인 `i+1`과 곱하여 `answer`를 업데이트 해주면 됩니다.

이전 배달에서 충족이 되었다면 while문을 통과하지 않아 `cnt`는 여전히 0이기 때문에 따로 예외처리 해주지 않아도 됩니다.

## 코드

```python
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver, pickup = 0, 0
    for i in range(n-1, -1, -1):
        deliver -= deliveries[i]
        pickup -= pickups[i]
        cnt = 0
        while deliver < 0 or pickup < 0:
            deliver += cap
            pickup += cap
            cnt += 1

        answer += (i+1)*2*cnt

    return answer
```
