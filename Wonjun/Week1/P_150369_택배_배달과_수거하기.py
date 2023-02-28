import math


def solution(cap, n, deliveries, pickups):
    cap_deliveries = [0] * n  # 배달하기 위해서 n개의 집을 몇 번 방문해야 하는가?
    cap_pickups = [0] * n  # 픽업하기 위해서 n개의 집을 몇 번 방문해야 하는가?
    for i in range(len(deliveries) - 1, -1, -1):  # 뒤에서부터 누적합
        if i == len(deliveries) - 1:
            deliveries[i] = deliveries[i]
        else:
            deliveries[i] = deliveries[i] + deliveries[i + 1]
        cap_deliveries[i] = math.ceil(deliveries[i] / cap)  # cap을 고려한 n개 집의 배달 방문 횟수 배열

    for i in range(len(pickups) - 1, -1, -1):
        if i == len(pickups) - 1:
            pickups[i] = pickups[i]
        else:
            pickups[i] = pickups[i] + pickups[i + 1]
        cap_pickups[i] = math.ceil(pickups[i] / cap)  # cap을 고려한 n개 집의 픽업 방문 횟수 배열

    temp = 0
    answer_deliveries = []  # 배달하기 위해 한번에 어디까지 가야하는가?
    answer_pickups = []  # 픽업하기 위해 한번에 어디까지 가야하는가?
    for i in range(n):
        if cap_deliveries[n - 1 - i] > temp:  # temp보다 크다면 즉, 배달하기 위한 방문 횟수가 변한다면
            for _ in range(cap_deliveries[n - 1 - i] - temp):  # 방문 해야하는 횟수대로
                answer_deliveries.append((n - i))  # 방문 거리를 append
            temp = cap_deliveries[n - 1 - i]  # 그리고 temp를 업데이트
    temp = 0
    for i in range(n):
        if cap_pickups[n - 1 - i] > temp:  # temp보다 크다면 즉, 픽업하기 위한 방문 횟수가 변한다면
            for _ in range(cap_pickups[n - 1 - i] - temp):
                answer_pickups.append((n - i))
            temp = cap_pickups[n - 1 - i]

    answer = 0
    # 픽업이 너무 많거나, 배달이 너무 많으면 둘의 방문 회차 수가 다르므로 0 배열로 맞춰 줌
    if len(answer_deliveries) > len(answer_pickups):
        answer_pickups.extend([0] * (len(answer_deliveries) - len(answer_pickups)))
    elif len(answer_deliveries) < len(answer_pickups):
        answer_deliveries.extend([0] * (len(answer_pickups) - len(answer_deliveries)))
    # 배달과 픽업 같은 회차에서 더 먼 곳까지 가면 나머지는 당연히 완료됨
    for i in range(len(answer_deliveries)):
        answer += 2 * max(answer_deliveries[i], answer_pickups[i])

    return answer


# 뒤에서부터 누적합을 하면...
# """
# 7 6 6 3 2 -> 4니까 7/4 = 1.x 2번은 가야됨... 4로 다 나눠보면? 1.x 1.x 1.x 0.x 0.x -> 올림 2 2 2 1 1
# 7 7 4 4 0 -> 4인데 얘도 2번... 1.x 1.x 1 1 0 -> 올림 2 2 1 1 0

# 일단 픽업이 딜리버리보다 큰 숫자가 없음. 즉 갔다가 오면서 다 해결됨
# 2 2 2 1 1 -> 1차 5거리까지            / 2차 3거리까지
# 2 2 1 1 0 -> 1차 5거리까지(위 따라감)  / 2차 3거리까지 ... 16 끝

# 5 3
# 4 2

# 6 5 5 3 3 2 2 ->
# 5 5 3 3 2 2 0 ->

# 2로 나눔 + 올림
# 여기도 딜리버리보다 큰 픽업은 없음
# 3 3 3 2 2 1 1 -> 1차 7까지 / 2차 5까지 / 3차 3까지
# 3 3 2 2 1 1 0 -> 1차 7까지 / 2차 5까지 /  3차 3까지 ... 14 + 10 + 6 = 30

# 7 5 3
# 6 4 2

# 만약 딜리버리보다 큰 픽업이 있다면? (그니까 한 집에 픽업할 게 개많음)
# 1 0 3 1 2 -> 7 6 6 3 2 -> 2 2 2 1 1
# 0 3 0 20 0 -> 23 23 20 20 0 -> 6 6 5 5 0

# 5 3
# 4 4 4 4 4 2

# """
