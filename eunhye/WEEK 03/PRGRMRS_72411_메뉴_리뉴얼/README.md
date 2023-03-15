## 풀이

orders의 크기도 20 이하이고, course의 숫자도 10 이하이기 때문에 가능한 모든 경우의 수를 다 찾아주었습니다.

모든 course에 대해 orders를 돌아주었습니다.
각 order로 구성할 수 있는 c개 코스를 combinations를 사용하여 찾아주었고,
찾아준 combi를 중복제거를 위해 sorted를 해준 뒤 string으로 변환하여 set에 넣어주었습니다.

그렇게 만들어진 subset으로 Counter인 cnt를 업데이트 해주었습니다.

orders를 다 돌고 나면, cnt에는 orders로 만들 수 있는 c개 코스들이 해당 조합을 주문한 손님의 수로 저장되어 있습니다.

cnt의 most_common을 사용하여 가장 선택을 많이 받은 조합의 순으로 정렬된 list를 저장해준 뒤,
해당 list를 돌아주며, 가장 많은 선택의 수를 받았으며, 2번 이상의 선택을 받은 모든 조합을 answer에 추가해줍니다.

이러한 과정을 앞에서 언급했듯이 모든 course 수에 대해 진행하게 되고,
마지막에는 answer를 sort하여 return해주면 됩니다.

## 코드

```python
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        cnt = Counter()
        for order in orders:
            subset = set(["".join(sorted(combi)) for combi in combinations(order, c)])
            cnt.update(subset)
        most_common = cnt.most_common()
        for menu, num in most_common:
            _, most_picked = most_common[0]
            if num == most_picked and num >= 2:
                answer.append(menu)
    answer.sort()
    return answer
```
