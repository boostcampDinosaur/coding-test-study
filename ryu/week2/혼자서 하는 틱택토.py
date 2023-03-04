# X가 O보다 많은 경우
# O가 X보다 두개이상 많은 경우
# O빙고가 완성됐는데 X의 개수가 같은경우
# X빙고가 완성됐는데 O가 더 많은 경우

def bingo_chk(board, mark):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True

    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True

    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == mark:
            return True

    return False


def solution(board):
    answer = -1

    o_count = 0
    x_count = 0
    for row in board:
        o_count += row.count("O")
        x_count += row.count("X")

    if x_count > o_count:  # X가 O보다 많은 경우
        return 0
    if o_count > x_count + 1:  # O가 X보다 두개이상 많은 경우
        return 0

    if bingo_chk(board, "O"):  # O빙고가 완성됐는데 X의 개수가 같은경우
        if x_count == o_count:
            return 0
    if bingo_chk(board, "X"):  # X빙고가 완성됐는데 O가 더 많은 경우
        if o_count > x_count:
            return 0

    return 1