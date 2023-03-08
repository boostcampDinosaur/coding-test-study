from collections import deque


def main():
    n = int(input())
    line = deque(map(int, input().split()))
    stack = []

    cur_n = 1
    while line or stack:
        # 줄 선거 그냥 들어가기
        if line and line[0] == cur_n:
            line.popleft()
            cur_n += 1
        # 옆으로 빼놓은 사람 들어가기
        elif stack and stack[-1] == cur_n:
            stack.pop()
            cur_n += 1
        # 옆으로 빼기
        elif line:
            stack.append(line.popleft())
        # 더이상 뺄 수도 없음
        else:
            break

    if cur_n == n + 1:
        print("Nice")
    else:
        print("Sad")


if __name__ == "__main__":
    main()
