# n, m이 너무 크다. 이진탐색으로 접근해보자.
# 결국 특정 범위 내의 모든 값들이 가능해 질 것.
# 행, 열에 대해서 최대, 최소 해서 4가지 경계값을 찾자.


def movement(n, m, cur_x, cur_y, query):
    command, dx = query
    if command == 0:
        cur_y = max(0, cur_y - dx)
    elif command == 1:
        cur_y = min(m - 1, cur_y + dx)
    elif command == 2:
        cur_x = max(0, cur_x - dx)
    elif command == 3:
        cur_x = min(n - 1, cur_x + dx)
    else:
        raise ValueError("command는 0~3 입니다.")

    return cur_x, cur_y


def get_end_point(n, m, start_x, start_y, queries):
    cur_x, cur_y = start_x, start_y
    for query in queries:
        cur_x, cur_y = movement(n, m, cur_x, cur_y, query)

    return cur_x, cur_y


def binary_search_row(n, m, target, queries, lowest, highest):
    other = 0  # row만 볼 때는 y는 상관 없음

    # lower bound 찾기
    lowerbound = n
    low = lowest
    high = highest

    # 이진탐색 시작
    while low <= high:
        mid = (low + high) // 2
        end, _ = get_end_point(n, m, mid, other, queries)

        if end == target:  # 목적지가 일치
            lowerbound = min(lowerbound, mid)
            high = mid - 1

        elif end < target:
            low = mid + 1
        else:
            high = mid - 1

    # upper bound 찾기
    upperbound = -1
    low = lowest
    high = highest

    # 이진탐색 시작
    while low <= high:
        mid = (low + high) // 2
        end, _ = get_end_point(n, m, mid, other, queries)

        if end == target:  # 목적지가 일치
            upperbound = max(upperbound, mid)
            low = mid + 1

        elif end < target:
            low = mid + 1
        else:
            high = mid - 1

    return lowerbound, upperbound


def binary_search_col(n, m, target, queries, lowest, highest):
    other = 0  # col만 볼 때는 x는 상관 없음

    # lower bound 찾기
    lowerbound = m
    low = lowest
    high = highest

    # 이진탐색 시작
    while low <= high:
        mid = (low + high) // 2
        _, end = get_end_point(n, m, other, mid, queries)

        if end == target:  # 목적지가 일치
            lowerbound = min(lowerbound, mid)
            high = mid - 1

        elif end < target:
            low = mid + 1
        else:
            high = mid - 1

    # upper bound 찾기
    upperbound = -1
    low = lowest
    high = highest

    # 이진탐색 시작
    while low <= high:
        mid = (low + high) // 2
        _, end = get_end_point(n, m, other, mid, queries)

        if end == target:  # 목적지가 일치
            upperbound = max(upperbound, mid)
            low = mid + 1

        elif end < target:
            low = mid + 1
        else:
            high = mid - 1

    return lowerbound, upperbound


def solution(n, m, x, y, queries):
    low_x = 0
    low_y = 0
    high_x = n - 1
    high_y = m - 1
    lower_x, upper_x = binary_search_row(n, m, x, queries, low_x, high_x)
    lower_y, upper_y = binary_search_col(n, m, y, queries, low_y, high_y)

    if lower_x == n or lower_y == m or upper_x == -1 or upper_y == -1:
        return 0
    return (upper_x - lower_x + 1) * (upper_y - lower_y + 1)
