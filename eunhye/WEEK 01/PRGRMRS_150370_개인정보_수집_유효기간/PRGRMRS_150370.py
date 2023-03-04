def solution(today, terms, privacies):
    result = []
    today_y, today_m, today_d = map(int, today.split("."))
    today = (today_y - 2000) * 12 * 28 + today_m * 28 + today_d

    terms = {term[0]: today - 28 * int(term[2:]) for term in terms}

    for idx, privacy in enumerate(privacies):
        p_date, p_term = privacy.split()
        p_year, p_month, p_day = map(int, p_date.split("."))
        collected_day = (p_year - 2000) * 12 * 28 + p_month * 28 + p_day

        if collected_day <= terms[p_term]:
            result.append(idx + 1)

    return result
