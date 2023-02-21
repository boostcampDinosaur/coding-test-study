import sys

input = sys.stdin.readline


def main():
    n = int(input())
    triangle = []
    dp_triangle = [[0 for _ in range(n + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        triangle.append(tuple(map(int, input().split())))

    for i, numbers in enumerate(triangle, 1):
        for j, number in enumerate(numbers, 1):
            dp_triangle[i][j] = (
                max(dp_triangle[i - 1][j], dp_triangle[i - 1][j - 1]) + number
            )

    print(max(dp_triangle[-1]))


if __name__ == "__main__":
    main()
