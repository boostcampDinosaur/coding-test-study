def solution(a, b, n):
    answer = 0

    while n > 1:
        recall = n // 2 * b
        answer += recall

        n = recall + n % a

    return answer

