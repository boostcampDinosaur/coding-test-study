## 풀이

동적계획법으로 풀어보겠습니다. 각 층의 숫자를 담은 `tri`는 예시 input일 경우에는 다음과 같습니다.

```
# tri[floor-1][nums]
[ [7],
  [3, 8],
  [8, 1, 0],
  [2, 7, 4, 4],
  [4, 5, 2, 6, 5] ]
```

다음은 `cache`인데 format은 `tri`와 같습니다. 다만 담아주는 값은 해당 숫자를 선택했을 때 최대 합을 담아줍니다.

첫 번째 층(`i=0`)는 하나밖에 없기에 무조건 선택이 됩니다. `tri`와 동일하게 초기화해준 뒤, 2번째 층 또한 최댓값이 자기 자신과 첫 번째 층 숫자 하나밖에 없기 때문에 첫 번째 층 숫자와 자기 자신을 더한 값을 저장해줍니다.

for loop을 2(세 번째 층)부터 `N`까지 돌려주며 각 층의 양 끝의 수(`i=0`, `i=N`)는 선택할 수 있는 이전 층의 최대 합이 이전 층의 양 끝의 수 하나씩 밖에 없으므로 두 번째 층에서 해준 것과 같이 먼저 값을 저장해줍니다.

해당 층의 중간에 위치한 수들을 위해 다시 for loop을 1부터 `i`까지 돌려주며 이전 층(`i-1`)의 왼쪽 대각선에 위치한 수(`cache[i-1][j-1]`)와 오른쪽 대각선에 위치한 수(`cache[i-1][j]`) 둘 중 최대합이 큰 것을 선택해 자기 자신(`tri[i][j]`)과 더해준 값을 저장해줍니다.

마지막으로 마지막 층(`cache[N-1]`)의 최대합 중 가장 큰 것을 골라 출력해줍니다.

## 코드

```python
N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]
cache = [[0 for _ in range(n+1)] for n in range(N)]
cache[0][0] = tri[0][0]
if N > 1:
    cache[1][0] = cache[0][0] + tri[1][0]
    cache[1][1] = cache[0][0] + tri[1][1]
    for i in range(2, N):
        cache[i][0] = cache[i-1][0] + tri[i][0]
        cache[i][i] = cache[i-1][i-1] + tri[i][i]
        for j in range(1, i):
            cache[i][j] = max(cache[i-1][j-1], cache[i-1][j]) + tri[i][j]
print(max(cache[N-1]))
```
