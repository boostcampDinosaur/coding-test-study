def solution(cap, n, deliveries, pickups):
    answer = 0

    remain_deliveries = sum(deliveries)
    remain_pickups = sum(pickups)
    end_delivery = n - 1
    end_pickup = n - 1

    while not deliveries[end_delivery] and end_delivery > 0:
        end_delivery -= 1

    while not pickups[end_pickup] and end_pickup > 0:
        end_pickup -= 1

    while remain_deliveries or remain_pickups:
        # 배달이나 픽업 해야하는 가장 먼곳으로 이동
        answer += (max(end_delivery, end_pickup) + 1) * 2

        # 배달하기
        boxes = min(cap, remain_deliveries)
        remain_deliveries -= boxes
        while True:
            need_to_delivery = deliveries[end_delivery]
            if need_to_delivery == 0:
                end_delivery -= 1
                continue

            if boxes == 0:
                break

            if boxes >= need_to_delivery:
                boxes -= need_to_delivery
                end_delivery -= 1
            else:
                deliveries[end_delivery] -= boxes
                boxes = 0

        # 수거하기
        capacities = min(cap, remain_pickups)
        remain_pickups -= capacities
        while True:
            need_to_pickup = pickups[end_pickup]
            if need_to_pickup == 0:
                end_pickup -= 1
                continue

            if capacities == 0:
                break

            if capacities >= need_to_pickup:
                capacities -= need_to_pickup
                end_pickup -= 1
            else:
                pickups[end_pickup] -= capacities
                capacities = 0

    return answer
