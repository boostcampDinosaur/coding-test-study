## 풀이

heapq를 이용하여 풀어주었습니다.

A팀의 순서가 정해져 있다고는 하지만, 우리가 찾고자 하는 답은 B팀이 얻을 수 있는 최대 승점이지, 최대 승점을 얻을 수 있는 B팀의 순서가 아닙니다.
따라서, B팀의 순서를 바꿀 수 있는 이상, A팀의 순서가 바뀌더라도 그에 맞게 B팀의 순서 또한 바꾸어주면 되므로, A팀의 순서를 고정할 필요가 없습니다.

이론상, A팀의 가장 작은 수를 가진 팀원부터 이기는 것이 최대 승점을 얻을 수 있는 방법이기 때문에, A팀 list를 heapq로 만들어 주어 하나씩 heappop하여 비교해주었습니다.

또한, A팀의 가장 작은 수를 가진 팀원보다 더 작은 숫자는 승점을 얻지 못하므로 제외해줍니다.
더 큰 숫자가 나타나면 heappop을 해줌과 동시에 cnt를 1 늘려주고 while문을 break해주면 cnt에는 B팀이 얻을 수 있는 최대 승점이 기록되게 됩니다.

## 코드

```python
from heapq import heapify, heappop

def solution(A, B):
    heapify(A)
    heapify(B)
    cnt = 0
    while A and B:
        A_member = heappop(A)
        while B:
            if B and B[0] > A_member:
                heappop(B)
                cnt += 1
                break
            heappop(B)

    return cnt
```
