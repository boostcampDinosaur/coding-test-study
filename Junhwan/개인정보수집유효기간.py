def parse_date(date: str) -> int:
    YYYY, MM, DD = map(int, date.split("."))
    # 어차피 차이만 계산. 한달이 28일.
    return 28 * 12 * YYYY + 28 * MM + DD


def check_expired(today: int, collect_date: str, valid_date: int) -> bool:
    collect_date = parse_date(collect_date)

    valid_date = 28 * valid_date

    if today >= collect_date + valid_date:
        return True
    return False


def solution(today, terms, privacies):
    answer = []

    today = parse_date(today)
    privacy_terms = dict()

    # 약관 저장
    for term in terms:
        AZ, valid_date = term.split()
        privacy_terms[AZ] = int(valid_date)

    # 개인정보 확인
    for i, privacy in enumerate(privacies, 1):
        collect_date, AZ = privacy.split()
        valid_date = privacy_terms[AZ]

        # 만료 되었으면 정답에 추가
        if check_expired(today, collect_date, valid_date):
            answer.append(i)

    return answer
