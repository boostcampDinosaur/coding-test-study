from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def bfs(maps, start, goal, visit):
    queue = deque()
    queue.append((start, 0))
    visit[100 * start[0] + start[1]] = True

    len_x = len(maps)
    len_y = len(maps[0])

    while queue:
        cur_xy, count = queue.popleft()
        cur_x, cur_y = cur_xy

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            next_pos = 100 * next_x + next_y

            # 범위 안에 있는 것만 고려
            if next_x < 0 or next_y < 0 or next_x >= len_x or next_y >= len_y:
                continue

            # 벽은 못감
            if maps[next_x][next_y] == "X":
                continue

            # 이미 와봤으면 가지 마
            if visit[next_pos]:
                continue

            # 목표 지점이면 탐색 종료
            if maps[next_x][next_y] == goal:
                return count + 1, (next_x, next_y)

            queue.append(((next_x, next_y), count + 1))
            visit[next_pos] = True

    # 도착 불가시 -1 return
    return -1, (0, 0)


def solution(maps):
    # 시작점 찾기
    for i, row in enumerate(maps):
        for j, value in enumerate(row):
            if value == "S":
                start = (i, j)

    # 레버 찾기
    goal = "L"
    visit = [False for _ in range(100**2)]

    count_l, pos_l = bfs(maps, start, goal, visit)

    if count_l == -1:
        return -1

    # 출구 찾기
    goal = "E"
    visit = [False for _ in range(100**2)]

    count_g, _ = bfs(maps, pos_l, goal, visit)

    if count_g == -1:
        return -1

    return count_l + count_g
