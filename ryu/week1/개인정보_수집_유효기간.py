def date_to_day(date, add_month=None): # day단위로 변환
    year, month, day = date.split(".")
    year, month, day = int(year), int(month), int(day)

    if add_month:
        month += add_month

    day = year * 12 * 28 + month * 28 + day

    return day


def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    today_day = date_to_day(today)  # 현재 날짜를 day단위로 변환

    for term in terms: # 유효기간을 dictionary형태로 저장
        name, month = term.split()
        terms_dict[name] = int(month)

    for i, privacy in enumerate(privacies): # 약관동의 날짜 추출
        date, terms = privacy.split() # 날짜와 약관 쪼갬
        privacy_day = date_to_day(date, terms_dict[terms]) # 약관동의 날짜 day단위로 변환하는데 약관에 해당하는 날짜 더해줌
        if today_day >= privacy_day: # 만약 오늘날짜 > 약관동의 날짜 + 약관에 해당하는 날짜 라면 answer append
            answer.append(i + 1)

    return answer