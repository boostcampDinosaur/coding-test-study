def solution(players, callings):
    rank_dict = dict()
    player_dict = dict()

    for rank, player in enumerate(players):
        rank_dict[rank] = player
        player_dict[player] = rank

    def swap(call_player):
        rank = player_dict[call_player]
        cur_player = rank_dict[rank - 1]

        player_dict[cur_player], player_dict[call_player] = rank, rank - 1
        rank_dict[rank], rank_dict[rank - 1] = cur_player, call_player

    for calling in callings:
        swap(calling)

    return list(rank_dict.values())