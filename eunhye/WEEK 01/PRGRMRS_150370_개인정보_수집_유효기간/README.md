## 풀이

우선, 년도가 2000년도 미만으로는 나타나지 않는다 하여 2000년 1월 1일을 기준으로 오늘 날짜까지의 일(day) 수로 바꾸어 주었습니다.

그 다음 약관의 종류와 유효기간을 `dict`로 바꾸어 주는데 이때 오늘 날짜에서 해당 유효기간을 빼주어 오늘 날짜 기준으로 유효기간을 알 수 있게 하였습니다.

그 다음은 `privacies`를 돌아주며 개인정보 수집 일자 또한 오늘 날짜와 동일한 방법으로 일 수로 변환한 뒤 `terms`에 저장된 유효기간 기준보다 작거나 같으면 `result`에 해당 번호를 `append`해주었습니다.

## 코드

```python
def solution(today, terms, privacies):
    result = []
    today_y, today_m, today_d = map(int, today.split("."))
    today = (today_y-2000)*12*28 + today_m*28 + today_d

    terms = {term[0]: today-28*int(term[2:]) for term in terms}

    for idx, privacy in enumerate(privacies):
        p_date, p_term = privacy.split()
        p_year, p_month, p_day = map(int, p_date.split("."))
        collected_day = (p_year-2000)*12*28 + p_month*28 + p_day

        if collected_day <= terms[p_term]:
            result.append(idx+1)

    return result
```
