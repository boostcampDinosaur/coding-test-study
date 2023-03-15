## 풀이

DP를 더한 DFS로 풀어주었습니다.

우선 2차원 배열 board에 input을 받아줍니다.
그리고 board와 같은 크기의 2차원 배열 cache를 -1의 값으로 초기화하여 만들어줍니다.

dfs 함수는 시작하는 좌표 sy, sx 두 개의 인자를 받으며,
만약 목표 지점에 도착했다면 1을 return합니다.

그렇지 않다면 sy, sx의 좌표를 cache를 확인하여 방문하였는지 확인해주고,
방문한 적이 있다면 더 진행하지 않고 cache[sy][sx] 값을 return해줍니다.

아직 방문하지 않았다면 (cache[sy][sx]가 초기화해준 -1 그대로라면) 0으로 방문표시를 한 뒤 상하좌우의 좌표를 체크해줍니다.
상하좌우가 범위 내에 있고, board값이 sy, sx 좌표의 board값보다 작다면 해당 좌표로 dfs 호출을 해주고 나온 return값을 cache[sy][sx]에 누적해줍니다.

마지막에는 dfs를 (0,0) 좌표를 출발 좌표로 호출하여 return되는 값을 출력해주면 됩니다.

## 코드

```python
N, M = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

board = [list(map(int, input().split())) for _ in range(N)]
cache = [[-1 for _ in range(M)] for _ in range(N)]


def dfs(sy, sx):
    if sy == N - 1 and sx == M - 1:
        return 1
    if cache[sy][sx] == -1:
        cache[sy][sx] = 0
        for i in range(4):
            ny, nx = sy + dy[i], sx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] < board[sy][sx]:
                cache[sy][sx] += dfs(ny, nx)
    return cache[sy][sx]


print(dfs(0, 0))

```
