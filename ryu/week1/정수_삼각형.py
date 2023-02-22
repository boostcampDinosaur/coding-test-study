# DP 로 해결

depth = int(input()) # 첫번째 줄은 삼각형의 깊이
triangle = list()
for i in range(depth): # 두번째 줄부터는 삼각형의 내용이므로 triangle list에 한줄씩 저장
    triangle.append(list(map(int, input().split())))

"""
  1
 2 3
1 4 5

  1
 3 4
4 8 9

이런 식으로 전개해나가는거라고 보면 됨 직전 row에서 자신에게 내려올 수 있는 값 중 가장 큰 값을 더해줌

여기서 주목해야될 것은 좌우 끝은 무조건 직전 row의 끝값들을 더하게된다.

즉 1. 왼쪽 끝값, 오른쪽 끝값, 중간 값을 고려하도록 짜면 됨
"""
for i, row in enumerate(triangle[1:], 1): # 첫번째 줄은 고정이므로 두번째 줄부터 계산
    for j in range(len(row)): # 현재 row의 길이만큼 돔
        if j == 0: # 왼쪽 끝값은 직전 왼쪽끝값을 더해줌
            triangle[i][j] += triangle[i - 1][j]
        elif j == len(row) - 1: # 오른쪽 끝값은 직전 오른쪽 끝값을 더해줌
            triangle[i][j] += triangle[i - 1][j - 1]
        else: # 중간 값을 자신에게 올 수 있는 직전 row의 값들 중 큰 값을 더해줌
            triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

print(max(triangle[depth - 1]))