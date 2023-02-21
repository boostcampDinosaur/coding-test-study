def solution(storey):
    answer = 0
    while storey:
        last_digit = storey % 10

        if last_digit < 5:
            storey -= last_digit
            answer += last_digit
        elif last_digit > 5:
            storey += 10 - last_digit
            answer += 10 - last_digit
        else:  # 딱 5인 경우는 다음 자리에 따라 달라짐
            next_digit = (storey // 10) % 10
            if next_digit > 4:
                storey += 10 - last_digit
                answer += 10 - last_digit
            else:
                storey -= last_digit
                answer += last_digit
        if storey % 10 != 0:
            raise ValueError("뭔가 이상한데?")

        storey = storey // 10

    return answer
