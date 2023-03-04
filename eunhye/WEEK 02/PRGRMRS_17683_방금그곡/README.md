## 풀이

## 코드

```python
# 시간을 분 단위로 환산합니다.
def str_to_int(s):
    h, m = map(int, s.split(":"))
    return h*60 + m

# #이 붙은 음을 처리해주며 string을 list로 바꿔줍니다.
def str_to_lst(s):
    lst = []
    for i in range(len(s)):
        if i+1 < len(s) and s[i+1] == "#":
            lst.append(s[i:i+2])
        elif s[i] != "#":
            lst.append(s[i])
    return lst

def solution(m, musicinfos):
    m_lst = str_to_lst(m)
    m_len = len(m_lst)
    answer = []
    for info in musicinfos:
        start, end, name, melody = info.split(",")
        # 재생시간
        play_time = str_to_int(end) - str_to_int(start)
        melody_lst = str_to_lst(melody)
        played = []
        # 음악의 길이보다 재생시간이 더 클 경우
        if len(melody_lst) < play_time:
            # 재생시간만큼 반복
            played += melody_lst*(play_time//len(melody_lst))
            played += melody_lst[:play_time%len(melody_lst)]
        else: # 재생시간과 같거나 음악의 길이가 더 길 경우
            # 재생시간만큼만 재생
            played = melody_lst[:play_time]
        # 네오의 멜로디길이만큼 list를 slice해 비교해줍니다.
        for i in range(play_time-m_len+1):
            # 찾으면 answer에 재생시간과 함께 넣어준 뒤 바로 break합니다.
            if played[i:i+m_len] == m_lst:
                answer.append((name, play_time))
                break
    # 재생시간으로 내림차순으로 정렬합니다. (큰 것이 앞으로)
    answer.sort(reverse=True, key=lambda x:x[1])
    # 찾았다면 가장 앞에 있는 곡의 제목 return
    if len(answer):
        return answer[0][0]
    # 찾지 못했을 때 "(None)" return
    return "(None)"
```
