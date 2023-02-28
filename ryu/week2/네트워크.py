from collections import deque


# bfs
def solution(n, computers):
    check_list = [0] * n
    queue = deque()
    answer = 0
    start_node = 0

    while 0 in check_list:  # 모든 노드를 돌 때 까지
        if check_list[start_node] == 0:  # 현재 노드가 아직 돌지 않은 곳이라면 bfs시작
            queue.append(start_node)
            while queue:
                node_num = queue.popleft()
                check_list[node_num] = 1

                for i in range(n):  # 현재 노드와 연결됐고 아직 지나치지 않은 모든 애들 queue에 담아줌
                    if check_list[i] == 0 and computers[node_num][i] == 1:
                        queue.append(i)
            answer += 1  # queue한 번 다 돌았다는 뜻은 네트워크하나라는 뜻이므로 answer + 1
        start_node += 1  # 시작 노드를 다음 노드로 바꿔줌

    return answer