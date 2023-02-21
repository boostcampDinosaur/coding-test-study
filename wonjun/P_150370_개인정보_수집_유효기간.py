def date_validation(yyyy, mm, dd):  # 날짜 유효성 검사 함수
    valid_d = dd
    valid_m = mm

    if dd == 0:  # join_d에서 1을 빼서 0이 될 수도 있음
        mm -= 1
        valid_d = 28
    if mm == 0:  # mm에서 1을 빼서 0이 될 수도 있음
        yyyy -= 1
        valid_m = 12

    valid_y, valid_m = (mm - 1) // 12, (mm - 1) % 12 + 1  # 유효한 (추가)year와 month
    valid_y = yyyy + valid_y

    # 이제 문자화하여 return
    valid_y = str(valid_y)

    if valid_m > 0 and valid_m < 10:
        valid_m = "0" + str(valid_m)

    if valid_d > 0 and valid_d < 10:
        valid_d = "0" + str(valid_d)

    return [valid_y, valid_m, valid_d]


def solution(today, terms, privacies):
    terms_dict = dict()
    answer = []
    today_y, today_m, today_d = today.split(".")  # 오늘 날짜 분해

    for term in terms:
        name, due = term.split()
        terms_dict[name] = int(due)  # {"약관 종류": 약관 기간} dict 생성

    for idx, privacy in enumerate(privacies):
        join_date, join_kind = privacy.split()  # 가입 날짜, 약관 종류
        join_y, join_m, join_d = map(int, join_date.split("."))  # 가입 날짜 분해

        # 가입 날짜에서 약관 종류에 따른 유효기간을 더한 날짜를 구하고, 이것이 오늘 날짜보다 지났는가 판단
        join_d -= 1  # 전날까지만 유효함
        join_m += terms_dict[join_kind]  # dict에서 찾아서 가입 month에 더함

        join_y1, join_m1, join_d1 = date_validation(
            join_y, join_m, join_d
        )  # 다만 유효하지 않은 날짜일 수 있으므로 유효성 검사 함수 호출

        if int("".join(map(str, [today_y, today_m, today_d]))) > int(
            "".join(map(str, [join_y1, join_m1, join_d1]))
        ):  # 오늘 날짜와 비교하기 위해 int형으로 변환 ex) 20220312 > 20220218
            answer.append(idx + 1)  # 지났다면 answer에 append

    return answer
