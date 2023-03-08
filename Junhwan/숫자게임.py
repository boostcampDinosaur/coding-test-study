from collections import deque


def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    A = deque(A)
    B = deque(B)

    while A:
        a = A.popleft()
        b = B.popleft()
        if b > a:
            answer += 1
        else:
            if B:
                # 질꺼면 최대한 크게 지자
                B.pop()
                B.appendleft(b)
            else:
                return answer
    return answer
