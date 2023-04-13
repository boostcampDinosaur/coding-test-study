def solution(names, yearnings, photos):
    answer = []
    score_dict = dict()

    for name, yearning in zip(names, yearnings):
        score_dict[name] = yearning

    for photo in photos:
        score_sum = 0
        for name in photo:
            if name in score_dict:
                score_sum += score_dict[name]

        answer.append(score_sum)

    return answer