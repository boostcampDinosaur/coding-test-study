def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse()
    pickups.reverse()

    delivery_count = 0
    pickup_count = 0
    for i, (delivery, pickup) in enumerate(zip(deliveries, pickups)):
        delivery_count += delivery
        pickup_count += pickup

        while delivery_count > 0 or pickup_count > 0:
            delivery_count -= cap
            pickup_count -= cap
            answer += (n - i) * 2

    return answer