def dfs(cnt, num):
    global answer
    if num == 0:
        answer = min(cnt, answer)
        return
    dist = num % 10
    if dist == 5:
        dfs(cnt + (10 - dist), (num + (10 - dist)) // 10)
        dfs(cnt + dist, (num - dist) // 10)
    elif dist > 5:
        dfs(cnt + (10 - dist), (num + (10 - dist)) // 10)
    else:
        dfs(cnt + dist, (num - dist) // 10)


def solution(storey):
    global answer
    answer = float("inf")
    dfs(0, storey)
    return answer
