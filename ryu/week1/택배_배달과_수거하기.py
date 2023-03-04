def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse() # 역으로 접근할 예정이므로 돌려줌
    pickups.reverse()

    delivery_count = 0
    pickup_count = 0
    for i, (delivery, pickup) in enumerate(zip(deliveries, pickups)): # 역으로 돌린 값을 하나씩 추출
        delivery_count += delivery # 배달할 값을 카운트
        pickup_count += pickup # 수거할 값을 카운트

        while delivery_count > 0 or pickup_count > 0: # 배송하거나 수거할 값이 존재한다면 while문 실행
            """
            현재지점 n-i에서 수거하거나 배달할 값에 capacity를 뻈는데도 값이 존재한다는 것은 그 지점에서 왕복할 필요가 있다는 뜻이다.
            따라서 매 반복마다 capacity를 빼주면서 값이 존재하는지 확인한다.
            """
            delivery_count -= cap # 배달할 값에서 용량만큼 뺌
            pickup_count -= cap # 수거할 값에서 용량만큼 뺌
            answer += (n - i) * 2 # 왕복이므로 2를 곱해서 answer 계산

    return answer
