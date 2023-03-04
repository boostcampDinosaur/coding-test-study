from collections import deque

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(src, dst, maps):
    maze = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    N, M = len(maze), len(maze[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == "X":
                maze[i][j] = -1

    queue = deque([src])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 0:
                maze[ny][nx] += maze[y][x] + 1
                queue.append((ny, nx))

    dst_y, dst_x = dst
    return maze[dst_y][dst_x]


def solution(maps):
    answer = 0
    S = (0, 0)
    L = (0, 0)
    E = (0, 0)

    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "L":
                L = (y, x)
            elif maps[y][x] == "S":
                S = (y, x)
            elif maps[y][x] == "E":
                E = (y, x)

    to_L = bfs(S, L, maps)
    to_E = bfs(L, E, maps)

    return to_L + to_E if to_L and to_E else -1
