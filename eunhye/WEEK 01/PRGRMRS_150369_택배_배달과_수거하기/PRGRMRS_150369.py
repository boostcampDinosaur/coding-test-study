def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver, pickup = 0, 0
    for i in range(n - 1, -1, -1):
        deliver -= deliveries[i]
        pickup -= pickups[i]
        cnt = 0
        while deliver < 0 or pickup < 0:
            deliver += cap
            pickup += cap
            cnt += 1

        answer += (i + 1) * 2 * cnt

    return answer
