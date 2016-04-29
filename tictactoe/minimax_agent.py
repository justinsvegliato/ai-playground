import tictactoe
import random

INITIAL_MOVES = [[0, 0], [0, 2], [2, 0], [2, 2]]

def get_score(board, active_player, depth):
    if tictactoe.has_won(board, active_player):
        return 10 - depth

    opponent = tictactoe.get_opponent(active_player)
    if tictactoe.has_won(board, opponent):
        return depth - 10

    return 0

def minimax(board, player, active_player, depth):
    if tictactoe.is_game_over(board):
        return None, get_score(board, active_player, depth)

    scores = []
    moves = []
    for move in tictactoe.get_available_moves(board):
        new_board = tictactoe.move(board, move[0], move[1], player)

        opponent = tictactoe.get_opponent(player)
        score = minimax(new_board, opponent, active_player, depth + 1)[1]

        scores.append(score)
        moves.append(move)

    best_value = max(scores) if player == active_player else min(scores)
    best_index = scores.index(best_value)

    return moves[best_index], scores[best_index]

def get_best_move(board, player):
    return minimax(board, player, player, 0)[0]

def get_initial_move():
    return random.choice(INITIAL_MOVES)