def date_to_day(date, add_month=None):
    year, month, day = date.split(".")
    year, month, day = int(year), int(month), int(day)

    if add_month:
        month += add_month

    day = year * 12 * 28 + month * 28 + day

    return day


def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    today_day = date_to_day(today)

    for term in terms:
        name, month = term.split()
        terms_dict[name] = int(month)

    for i, privacy in enumerate(privacies):
        date, terms = privacy.split()
        privacy_day = date_to_day(date, terms_dict[terms])
        if today_day >= privacy_day:
            answer.append(i + 1)

    return answer