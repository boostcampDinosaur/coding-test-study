import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def dfs(n, m, height_tables, dp_tables, cur_x, cur_y):
    cur_h = height_tables[cur_x][cur_y]

    for k in range(4):
        # 상하좌우에서 더해오기
        near_x = cur_x + dx[k]
        near_y = cur_y + dy[k]

        if near_x < 0 or near_x >= n or near_y < 0 or near_y >= m:
            continue

        # 더 낮은 곳에서는 올 수 없음
        near_h = height_tables[near_x][near_y]
        if near_h <= cur_h:
            continue

        # 이미 해당 방향 정보가 업데이트 된 경우
        if dp_tables[cur_x][cur_y][k]:
            continue

        dp_tables[cur_x][cur_y][4] += dfs(
            n, m, height_tables, dp_tables, near_x, near_y
        )
        dp_tables[cur_x][cur_y][k] = True

    return dp_tables[cur_x][cur_y][4]


def main():
    n, m = map(int, input().split())
    height_tables = tuple(tuple(map(int, input().split())) for i in range(n))

    # 해당 방향에서 값을 업데이트 한 적이 있는지 확인해야함
    dp_tables = [[[False, False, False, False, 0] for _ in range(m)] for __ in range(n)]
    dp_tables[0][0][4] = 1
    dfs(n, m, height_tables, dp_tables, n - 1, m - 1)

    print(dp_tables[n - 1][m - 1][4])


if __name__ == "__main__":
    main()
