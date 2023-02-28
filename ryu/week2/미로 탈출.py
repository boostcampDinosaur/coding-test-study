from collections import deque

# bfs
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(maps, start, end):
    x_len, y_len = len(maps[0]), len(maps)
    map_check = [[0 for _ in range(x_len)] for _ in range(y_len)]  # 이미 지나간 길인지 체크

    for i, row in enumerate(maps):  # 시작 지점 지정
        for j, value in enumerate(row):
            if value == start:
                start_x, start_y = j, i

    queue = deque()
    queue.append((start_x, start_y, 0))  # 시작지점 x, 시작지점 y, 소요시간 queue에 저장
    map_check[start_y][start_x] = 1  # 시작지점 지나간걸로 표시

    while queue:  # bfs 시작
        x, y, second = queue.popleft()

        if maps[y][x] == end:  # end 부분 도착하면 바로 리턴
            return second

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if (0 <= nx < x_len) and (0 <= ny < y_len):
                if (map_check[ny][nx] == 0 and not maps[ny][nx] == "X"):
                    queue.append((nx, ny, second + 1))
                    map_check[ny][nx] = 1

    return -1  # 큐를 전부 돌았는데도 없다면 -1


def solution(maps):
    answer = 0

    lever_distance = bfs(maps, "S", "L")
    exit_distance = bfs(maps, "L", "E")

    if lever_distance == -1 or exit_distance == -1:  # 두 경로 중 하나라도 안된다면 -1을 리턴
        return -1
    else:
        return lever_distance + exit_distance
