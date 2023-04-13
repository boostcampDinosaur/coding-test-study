def solution(wallpaper):
    start_i, start_j, end_i, end_j = 51, 51, -1, -1

    for i, row in enumerate(wallpaper):
        for j, value in enumerate(row):
            if value == "#":
                if start_i > i:
                    start_i = i
                if start_j > j:
                    start_j = j
                if end_i < i + 1:
                    end_i = i + 1
                if end_j < j + 1:
                    end_j = j + 1

    return [start_i, start_j, end_i, end_j]