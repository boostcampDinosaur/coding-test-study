def solution(n, m, section):
    answer = 1
    paint = section[0] + m - 1

    for point in section:
        if paint < point:
            paint = point + m - 1
            answer += 1

    return answer