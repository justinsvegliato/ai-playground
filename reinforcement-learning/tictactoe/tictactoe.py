import numpy as np
import random

EMPTY_SQUARE = 0
FIRST_PLAYER = 1
SECOND_PLAYER = 2

PLAYER_SYMBOLS = ["-", "X", "O"]

def get_empty_board():
    return np.matrix("0, 0, 0; 0, 0, 0; 0, 0, 0")

def get_board_size(board):
    return len(board)

def get_available_moves(board):
    size = get_board_size(board)

    moves = []
    for x in range(size):
        for y in range(size):
            if is_valid_move(board, x, y):
                moves.append([x, y])

    return moves

def move(board, x, y, player):
    board[x, y] = player

def has_won(board, player):
    size = get_board_size(board)

    for i in range(size):
        if np.all(board[i] == player) or np.all(board[:, i] == player):
            return True

    return np.all(np.diagonal(board) == player) or np.all(np.diagonal(np.fliplr(board)) == player)

def is_board_full(board):
    return len(get_available_moves(board)) == 0

def is_game_over(board):
    return has_won(board, FIRST_PLAYER) or has_won(board, SECOND_PLAYER) or is_board_full(board)

def is_valid_move(board, x, y):
    return board[x, y] == EMPTY_SQUARE

def display_board(board):
    size = get_board_size(board)

    for x in range(size):
        for y in range(size):
            print PLAYER_SYMBOLS[board[x, y]],
        print ""

def get_players():
    human_player = random.choice([FIRST_PLAYER, SECOND_PLAYER])
    return (human_player, SECOND_PLAYER) if human_player == FIRST_PLAYER else (human_player, FIRST_PLAYER)