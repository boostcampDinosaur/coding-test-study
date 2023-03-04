from collections import deque


def BFS(graph, point, visited):
    queue = deque([point])
    visited[point] = 1

    while queue:
        v = queue.popleft()
        for idx, vertex in enumerate(graph[v]):  # 네트워크로 연결되어 있다면 queue에 추가
            if vertex == 1 and visited[idx] == 0:
                queue.append(idx)
                visited[idx] = 1


def solution(n, computers):
    visited = [0] * n  # 컴퓨터의 수만큼 방문기록
    answer = 0
    while 0 in visited:  # 방문하지 않은 컴퓨터가 있는 동안에 반복
        answer += 1  # 반복할 때마다 정답 1 추가
        point = visited.index(0)  # 방문하지 않은 가장 앞의 컴퓨터
        BFS(computers, point, visited)

    return answer


# 27
"""
1 1 0
1 1 0
0 0 1

1 1 0
1 1 1
0 1 1
"""
# BFS로 접근, 이어진 것들을 인접 노드로 queue에 등록한다.\

# * visited[idx]로 해야하는데 visited[vertex]로 하고 있어서 헤맴: 왜 그랬을까.... 정신차리자.

# 교훈
# 유니온파인드
