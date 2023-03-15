from heapq import heapify, heappop


def solution(A, B):
    heapify(A)
    heapify(B)
    cnt = 0
    while A and B:
        A_member = heappop(A)
        while B:
            if B and B[0] > A_member:
                heappop(B)
                cnt += 1
                break
            heappop(B)

    return cnt
