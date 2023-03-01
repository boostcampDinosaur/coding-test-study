def find_root(networks, i):
    # 자기 자신과 동일하면 자신이 루트
    if networks[i] != i:
        networks[i] = find_root(networks, networks[i])

    return networks[i]


def solution(n, computers):
    # 유니온 파인드로 풀자
    networks = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            # i, j가 연결이 안된 경우 패스
            if computers[i][j] != 1:
                continue

            # 연결 됐으면 더 작은 루트로 연결
            root_i = find_root(networks, i)
            root_j = find_root(networks, j)

            networks[root_i] = min(root_i, root_j)
            networks[root_j] = min(root_i, root_j)

    for i in range(n):
        networks[i] = find_root(networks, i)

    return len(set(networks))
