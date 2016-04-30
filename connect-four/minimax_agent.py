import connect_four

MAX_DEPTH = 4

WEIGHT_MAP = [[3, 4, 5, 7, 5, 4, 3],
              [4, 6, 8, 10, 8, 6, 4],
              [5, 8, 11, 13, 11, 8, 5],
              [5, 8, 11, 13, 11, 8, 5],
              [4, 6, 8, 10, 8, 6, 4],
              [3, 4, 5, 7, 5, 4, 3]]

def get_score(board, active_player):
    opponent = connect_four.get_opponent(active_player)
    if connect_four.get_winner(board) == opponent:
        return float("-inf")

    if connect_four.get_winner(board) == active_player:
        return float("inf")

    score = 0

    for row in range(connect_four.ROWS):
        for column in range(connect_four.COLUMNS):
            if connect_four.get_cell(board, row, column) == active_player:
                score += WEIGHT_MAP[row][column]
            elif connect_four.get_cell(board, row, column) == opponent:
                score -= WEIGHT_MAP[row][column]

    return score

def minimax(board, player, active_player, depth):
    if depth >= MAX_DEPTH or connect_four.get_winner(board):
        return None, get_score(board, active_player)

    scores = []
    moves = []
    for move in connect_four.get_available_moves(board):
        new_board = connect_four.move(board, player, move)

        opponent = connect_four.get_opponent(player)
        score = minimax(new_board, opponent, active_player, depth + 1)[1]

        scores.append(score)
        moves.append(move)

    best_value = max(scores) if player == active_player else min(scores)
    best_index = scores.index(best_value)

    return moves[best_index], scores[best_index]

def get_best_move(board, player):
    return minimax(board, player, player, 0)[0]