def process_sharp(melodies: str) -> list:
    """
    A~G랑 #이 같이 있으니까 #이 뒤에 있는 경우를 처리해서 리스트로 반환
    C랑 C#이 구분이 안되니까 C#같은 경우 C를 c로 변환
    """
    stack = []
    for melody in melodies:
        if melody == "#":
            stack[-1] = stack[-1].lower() + melody
        else:
            stack.append(melody)

    return stack


def hhmm2min(time: str) -> int:
    """
    시간을 분단위로 변환
    """
    hh, mm = map(int, time.split(":"))
    return hh * 60 + mm


def process_music_info(start_time: str, end_time: str, music_info: str):
    # 시간 변환
    start_time = hhmm2min(start_time)
    end_time = hhmm2min(end_time)
    play_time = end_time - start_time

    # #처리
    music_info = process_sharp(music_info)
    music_len = len(music_info)

    # 노래가 몇번 나왔는지 들린 그대로 반환
    play_count = play_time // music_len
    remain = play_time % music_len

    return music_info * play_count + music_info[:remain], play_time


def solution(m, musicinfos):
    answer = []
    m = "".join(process_sharp(m))
    for i, musicinfo in enumerate(musicinfos):
        start_time, end_time, title, music_info = musicinfo.split(",")
        music_info, play_time = process_music_info(start_time, end_time, music_info)
        music_info = "".join(music_info)
        if m in music_info:
            answer.append((play_time, i, title))

    if not answer:
        return "(None)"

    answer.sort(key=lambda x: (-x[0], x[1]))
    return answer[0][2]
