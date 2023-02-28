def is_game_over(board):
    board = ["".join(row) for row in board]
    if "OOO" in board or "XXX" in board:
        return 1

    board_t = ["".join(b) for b in zip(*board)]
    if "OOO" in board_t or "XXX" in board_t:
        return 1

    neg_diag = board[0][0] + board[1][1] + board[2][2]
    if neg_diag == "OOO" or neg_diag == "XXX":
        return 1

    pos_diag = board[0][2] + board[1][1] + board[2][0]
    if pos_diag == "OOO" or pos_diag == "XXX":
        return 1
    return 0


def backtrack(turn, new_board, O_player, X_player):
    if not O_player and not X_player:
        return 1
    if is_game_over(new_board):
        return 0 if O_player or X_player else 1

    if turn:
        if not O_player:
            return 0
        for i, (y, x) in enumerate(O_player):

            new_board[y][x] = "O"
            result = backtrack(
                0 if turn else 1, new_board, O_player[:i] + O_player[i + 1 :], X_player
            )
            if result:
                return 1
            new_board[y][x] = "."
    else:
        if not X_player:
            return 0
        for i, (y, x) in enumerate(X_player):

            new_board[y][x] = "X"
            result = backtrack(
                0 if turn else 1, new_board, O_player, X_player[:i] + X_player[i + 1 :]
            )
            if result:
                return 1
            new_board[y][x] = "."
    return 0


def solution(board):
    answer = 1
    O_player, X_player = [], []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                O_player.append((i, j))
            elif board[i][j] == "X":
                X_player.append((i, j))

    new_board = [list("...") for _ in range(3)]
    turn = 1

    return backtrack(turn, new_board, O_player, X_player)
