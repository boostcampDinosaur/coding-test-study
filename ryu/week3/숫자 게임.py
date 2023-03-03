# 당연히 자기가 가진 수 중에서 상대 수보다 크면서 차이가 많이 안나는 걸 써야됨
# 둘 다 내림차순 정렬하고 B가 이길 경우에만 idx 증가

def solution(A, B):
    answer = 0

    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)

    b_idx = 0
    for a_num in A:
        if a_num < B[b_idx]:
            answer += 1
            b_idx += 1

    return answer