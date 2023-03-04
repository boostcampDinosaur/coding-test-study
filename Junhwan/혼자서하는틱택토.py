from collections import Counter


def check_miss_OX(board):
    counter = Counter()

    for row in board:
        counter.update(row)

    count_O = counter["O"]
    count_X = counter["X"]

    if count_O == count_X:  # 동일한 경우는 1
        return 1
    elif count_O == count_X + 1:  # 1 차이나면 2
        return 2
    else:
        return 0  # 불가능하면 0


def check_already_won(board, count_ox):
    if count_ox == 0:
        return False

    count_win_horizontal = [0, 0]
    count_win_vertical = [0, 0]
    count_win_cross = [0, 0]

    # 가로 방향 확인
    for row in board:
        if len(set(row)) == 1 and row[0] != ".":
            if row[0] == "O":
                count_win_horizontal[0] += 1
            else:
                count_win_horizontal[1] += 1

    # 세로 방향 확인
    for col in zip(*board):
        if len(set(col)) == 1 and col[0] != ".":
            if col[0] == "O":
                count_win_vertical[0] += 1
            else:
                count_win_vertical[1] += 1

    # 대각선 확인
    p1, p2, p3 = board[0][0], board[1][1], board[2][2]
    if len(set([p1, p2, p3])) == 1 and p1 != ".":
        if p1 == "O":
            count_win_cross[0] += 1
        else:
            count_win_cross[1] += 1

    p1, p2, p3 = board[0][2], board[1][1], board[2][0]
    if len(set([p1, p2, p3])) == 1 and p1 != ".":
        if p1 == "O":
            count_win_cross[0] += 1
        else:
            count_win_cross[1] += 1

    # 두개 이상의 가로, 혹은 세로줄이 있으면 안됨
    if sum(count_win_horizontal) >= 2 or sum(count_win_vertical) >= 2:
        return False

    # O가 선공이니까 O의 승리인 경우 X의 돌의 개수와 같으면 안됨
    if count_win_horizontal[0] == 1 and count_ox == 1:
        return False
    if count_win_vertical[0] == 1 and count_ox == 1:
        return False
    if count_win_cross[0] == 1 and count_ox == 1:
        return False

    # 반대로 X의 승리인 경우 O의 개수가 더 많으면 안됨
    if count_win_horizontal[1] == 1 and count_ox == 2:
        return False
    if count_win_vertical[1] == 1 and count_ox == 2:
        return False
    if count_win_cross[1] == 1 and count_ox == 2:
        return False

    return True


def solution(board):
    answer = -1
    counter = Counter()

    for row in board:
        counter.update(row)

    count_ox = check_miss_OX(board)

    answer = check_already_won(board, count_ox)

    return int(answer)
