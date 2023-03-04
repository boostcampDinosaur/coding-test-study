def remove_hash(notes):  # replace를 써도 되겠다.
    """
    notes에서 #이 붙은 음은 소문자로 변환해 notes_transform를 반환
    """
    notes_transform = []  # stack 구조
    for note in notes:
        if note == "#":
            notes_transform.append(notes_transform.pop().lower())
        else:
            notes_transform.append(note)
    return "".join(notes_transform)


def solution(m, musicinfos):
    music_dict = dict()
    m = remove_hash(m)  # m에서 # 제거

    for music in musicinfos:
        start, end, name, notes = music.split(",")
        notes = remove_hash(notes)  # notes에서 # 제거
        time = (int(end[0:2]) * 60 + int(end[3:5])) - (
            int(start[0:2]) * 60 + int(start[3:5])
        )
        streaming = (
            notes * (time // (len(notes))) + notes[0 : (time % len(notes))]
        )  # 실제 재생된 음
        music_dict[name] = streaming  # dict에 {"제목" : "실제 재생된 음"}으로 저장

    find_music = "(None)"  # 이 부분을 신경쓰지 않아서 헤맴
    max_length = 0
    for n, s in music_dict.items():
        if m in s and len(s) > max_length:
            find_music = n
            max_length = len(s)
    return find_music


# 들은 음은 1439개 이하의 음으로 구성된 문자열
# 음악 제목은 64이하의 문자열
# 악보 정보는 1439개 이하의 음으로 구성된 문자열
# #이 붙은 음도 있는데, 길이 계산에서 고려해야 함 -> 차라리 # 붙은 음을 소문자로 표기하자.

# * 자정을 넘기는 것을 고려, 일치하지 않을 경우 아무것도 안 함, 제일 긴 음악 제목... 무시해서 헤맴: 조건을 하나도 읽지 않아서 생긴 문제... 왜 그랬을까?
