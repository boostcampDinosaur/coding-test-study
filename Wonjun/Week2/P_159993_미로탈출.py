from collections import deque


def search_point(maps, point):  # S, L, E 찾는 함수
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == point:
                return [i, j]


def BFS(maps, start, visited, goal):  # 시작점, 목표점 입력하여 BFS 탐색
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([start])
    visited[start[0]][start[1]] = 0

    while queue:
        v = queue.popleft()
        if maps[v[0]][v[1]] == goal:  # 목표점에 도달
            return visited[v[0]][v[1]]

        for m in move:
            next_r = v[0] + m[0]
            next_c = v[1] + m[1]
            if next_r in range(0, len(maps)) and next_c in range(0, len(maps[0])):
                if (
                    maps[next_r][next_c] in "SOLE" and visited[next_r][next_c] == -1
                ):  # SOLE 모두 밟을 수 있음
                    queue.append([next_r, next_c])
                    visited[next_r][next_c] = visited[v[0]][v[1]] + 1
    return -1  # 목표점에 도달하지 못함


def solution(maps):
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]  # visited는 -1 이중 리스트
    answer = 0  # S에서 L에서 E로 가는 길
    answer += BFS(maps, search_point(maps, "S"), visited, "L")
    if answer < 0:  # 고립된 Start
        return -1
    LtoE = 0  # L에서 E로 가는 길
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]  # visited 초기화
    LtoE_route = BFS(maps, search_point(maps, "L"), visited, "E")  # E에 도달할 수 없는 경우 -1
    answer += LtoE_route
    LtoE += LtoE_route

    return answer if LtoE > 0 else -1


# * SOLE을 모두 밟을 수 있다는 것: 일반적인 BFS의 경우 O X밖에 없고, O 모두 밟을 수 있음. 그렇다면 이런 문제에서는 당연히 SOLE 모두 밟을 수 있다고 해야 함. BFS의 변형!
# * visited 초기화를 해야 함: 여기서 여기 갔다가, 다시 그걸 시작점으로 잡자는 생각... 그럼 당연히 모든 조건 초기화하고 가야함
# * 도달할 수 없는 경우: LtoE 변수를 따로 둬서 해결. 다만 모든 BFS 문제에서 이렇게 끊겨있는 경우를 일단 염두에 두자.
