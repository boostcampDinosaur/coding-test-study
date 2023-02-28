def replace_melody(m):  # 반복문으로 늘릴 때 귀찮으니 한개로 통일
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")

    return m


def get_music_time(start_time, end_time):  # 분으로 계산
    start_hour, start_minute = start_time.split(":")
    end_hour, end_minute = end_time.split(":")

    start_time = int(start_hour) * 60 + int(start_minute)
    end_time = int(end_hour) * 60 + int(end_minute)

    return end_time - start_time


def solution(m, musicinfos):
    answer = ''
    max_time = -1
    m = replace_melody(m)

    for musicinfo in musicinfos:
        start_time, end_time, music_name, music_m = musicinfo.split(',')
        music_m = replace_melody(music_m)  # 샾제거
        music_time = get_music_time(start_time, end_time)  # 음악길이 계산

        cnt = 0
        full_music_m = ''
        while cnt < music_time:  # 음악길이만큼 반복
            full_music_m += music_m[cnt % len(music_m)]  # 음을 음악길이에 맞게 늘려줌
            cnt += 1

        if m in full_music_m and max_time < music_time:  # 최초 음이 음악안에 들어있으며 지금까지 일치한 음악 중 길이가 가장 길다면 다시 설정
            max_time = music_time
            answer = music_name

    if answer == '':  # 없으면 (None)
        answer = "(None)"
    return answer