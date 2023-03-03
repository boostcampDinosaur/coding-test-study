# bfs, 우선순위 큐 사용
# 단순하게 bfs로만 풀면 특정 위치에서 전진할 수 있는 경우의 수 중 가장 낮은 데를 먼저 가버리면 다른 곳이 카운팅안됨 예를 들어
"""
5 4
2 3
1

이렇게 있을 때 1로 가는 경우가 (5 -> 2 -> 1), (5 -> 4 -> 3 -> 2 -> 1) 총 두 가지 경우가 있지만 1에 전파 되는 건 5 -> 2 -> 1밖에 없음
"""

import heapq

n, m = map(int, input().split())

maps = list()
for _ in range(n):
    maps.append(list(map(int, input().split())))

move_points = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    visited = [[0] * m for _ in range(n)]
    queue = list()
    queue.append((-maps[0][0], 0, 0))
    visited[0][0] = 1

    while queue:
        h, y, x = heapq.heappop(queue)
        h *= -1

        if y == (n - 1) and x == (m - 1):
            continue

        for mx, my in move_points:
            nx = x + mx
            ny = y + my

            if (0 <= nx < m) and (0 <= ny < n):
                nh = maps[ny][nx]
                if nh < h:
                    if visited[ny][nx] == 0:
                        heapq.heappush(queue, (-nh, ny, nx))
                    visited[ny][nx] += visited[y][x]

    return visited[n - 1][m - 1]

result = bfs()
print(result)