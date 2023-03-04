def solution(storey):
    answer = 0

    while storey:
        num = storey % 10

        # 5인 경우 다음 자릿수가 5보다 크면 10으로 아니라면 0으로 마법의돌 써야됨
        if num == 5:
            next_num = (storey // 10) % 10
            if next_num >= 5:
                storey += 10
            answer += num
        # 5보다 큰경우 10을 향해 마법의 돌을 씀
        elif num > 5:
            answer += (10 - num)
            storey += 10
        # 5보다 작은경우 0을 향해 마법의 돌 사용
        else:
            answer += num

        storey //= 10

    return answer