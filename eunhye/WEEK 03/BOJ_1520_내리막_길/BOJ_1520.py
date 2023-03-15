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
