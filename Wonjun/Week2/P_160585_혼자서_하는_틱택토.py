from collections import deque


def count_number(board):
    """
    O_nums < X_nums -> -1
    O_nums > X_nums + 1 -> -1
    O_nums = X_nums -> 0
    O_nums > X_nums -> 1
    """
    O_nums, X_nums = 0, 0
    for row in board:
        O_nums += row.count("O")
        X_nums += row.count("X")
    return (
        -1
        if (O_nums - X_nums > 1 or X_nums > O_nums)
        else (0 if O_nums == X_nums else 1)
    )


def judge_winlose(board, target):
    """
    target으로 입력한 문자가 승리할 수 있다면 True, 그렇지 않다면 False

    target인 시작점에서 move로 한 칸 범위의 주변을 탐색하여 target이라면 그 방향으로 한 칸 더 탐색
    만약 세 개가 만족한다면 승리 조건
    """
    move = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
        [1, 1],
        [1, -1],
        [-1, -1],
        [-1, 1],
    ]  # 움직이는 경우의 수
    target_rc = deque([])
    for i in range(3):
        for j in range(3):
            if board[i][j] == target:
                target_rc.append([i, j])  # target의 위치를 모두 탐색

    for rc in target_rc:  # 그들을 차례로 시작점으로 설정해 승리할 수 있는지 확인
        for m in move:
            next_r = rc[0] + m[0]
            next_c = rc[1] + m[1]
            if (
                next_r in range(0, 3)
                and next_c in range(0, 3)
                and board[next_r][next_c] == target
            ):
                if (
                    next_r + m[0] in range(0, 3)
                    and next_c + m[1] in range(0, 3)
                    and board[next_r + m[0]][next_c + m[1]] == target
                ):
                    return True
    return False


def solution(board):
    OX_nums = count_number(board)  # 각 문자의 개수를 세어 비교
    O_win = judge_winlose(board, "O")  # O가 승리한다면 True, 아니면 False
    X_win = judge_winlose(board, "X")  # X가 승리한다면 True, 아니면 False

    if OX_nums == -1:  # X가 더 많은 경우, 혹은 O가 1개 초과 많은 경우 원초적으로 불가능
        return 0
    elif all([O_win, X_win]):  # 둘 다 승리조건을 만족하는 경우 원초적으로 불가능
        return 0
    elif OX_nums == 1 and X_win:  # X 승리지만 O가 하나 더 둔 경우
        return 0
    elif OX_nums == 0 and O_win:  # O 승리지만 X가 하나 더 둔 경우
        return 0
    else:
        return 1


# 1. 정상적인 상황이 무엇인지 파악
# -> 다 찼다면 X 4개  O 5개가 정상일 것, 다 차지 않더라도 둘의 개수는 1개 또는 0개 차이, 항상 O 개수 >= X 개수이고 1개 초과 크지 않음
# * O 개수가 2개 이상 X보다 많을 수 있다는 경우를 고려하지 않아서 헤맴: 문제 조건을 다 써놓고 하나씩 만족할 수 있게 해야함.
# -> 한 쪽이 한 줄 완성으로 끝났다면 다른 한 쪽은 절대 완성할 수 없음
# -> 게임이 끝났는데 또 놓을 수는 없음. 즉, 둘의 숫자가 같더라도 틀린 경우일 수 있다는 것

# board의 크기는 3x3이라 어떻게 탐색하든 상관없음
# 개수만을 탐색하는 함수 + 게임이 종료되었는지 탐색하는 함수
# 승리 조건 탐색하는 함수는 BFS? -> 아니 일직선으로 탐색하는 게 낫지. DFS? -> 잠만 꺾여있으면 안 되잖아. -> 그냥 탐색으로 가자
