int_triangle = []
for i in range(int(input())):
    int_triangle.append(list(map(int, input().split())))

# 현재 칸의 최고 점수는 max(현재 칸 값 + 이전 왼쪽 칸 값, 현재 칸 값 + 이전 오른쪽 칸 값)
for row in range(1, len(int_triangle)):
    for num in range(row + 1):  # 모든 행 탐색
        if num == 0:  # 가장 왼쪽 줄
            int_triangle[row][num] = int_triangle[row][num] + int_triangle[row - 1][num]
        elif num == row:  # 가장 오른쪽 줄
            int_triangle[row][num] = (
                int_triangle[row][num] + int_triangle[row - 1][num - 1]
            )
        else:  # 중간 줄
            int_triangle[row][num] = max(
                int_triangle[row][num] + int_triangle[row - 1][num],
                int_triangle[row][num] + int_triangle[row - 1][num - 1],
            )

print(max(int_triangle[-1]))


# 최대 2의 500승 만큼의 경우의 수가 생겨서 모든 것을 탐색하는 것은 불가능
# Greedy? 둘 중 큰 것만 찾아가는 것은 불가능. 다음 작은 수의 다다음 수가 매우 큰 숫자일 경우를 캐치하지 못함
# BFS? 최적의 루트를 찾는 것과 같으므로...
# 백트래킹? 다음 걸 선택 -> 다다음 걸 보고 발빼기... 그럼 다다다음 것이 가장 큰 수라면 그것을 캐치하지 못함
# DP? 500칸이 있더라도, 반복하는 것이 아니라 각 칸을 보겠다면, 삼각형이라서 500 * 500 보단 작은 경우의 수이므로 탐색 가능. 또한 점화식이 보임
