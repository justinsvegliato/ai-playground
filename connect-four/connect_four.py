from termcolor import colored
import numpy as np
import random

COLUMNS = 7
ROWS = 6

EMPTY_CELL = 0
FIRST_PLAYER = 1
SECOND_PLAYER = 2

CIRCLE_SYMBOL = u"\u25cf"
EMPTY_CELL_COLOR = "grey"
FIRST_PLAYER_COLOR = "red"
SECOND_PLAYER_COLOR = "green"
SYMBOLS = [colored(u"\u25a0", EMPTY_CELL_COLOR),
           colored(CIRCLE_SYMBOL, FIRST_PLAYER_COLOR),
           colored(CIRCLE_SYMBOL, SECOND_PLAYER_COLOR)]

WINNING_POSITIONS = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                     [(0, 1), (0, 2), (0, 3), (0, 4)],
                     [(0, 2), (0, 3), (0, 4), (0, 5)],
                     [(0, 3), (0, 4), (0, 5), (0, 6)],
                     [(1, 0), (1, 1), (1, 2), (1, 3)],
                     [(1, 1), (1, 2), (1, 3), (1, 4)],
                     [(1, 2), (1, 3), (1, 4), (1, 5)],
                     [(1, 3), (1, 4), (1, 5), (1, 6)],
                     [(2, 0), (2, 1), (2, 2), (2, 3)],
                     [(2, 1), (2, 2), (2, 3), (2, 4)],
                     [(2, 2), (2, 3), (2, 4), (2, 5)],
                     [(2, 3), (2, 4), (2, 5), (2, 6)],
                     [(3, 0), (3, 1), (3, 2), (3, 3)],
                     [(3, 1), (3, 2), (3, 3), (3, 4)],
                     [(3, 2), (3, 3), (3, 4), (3, 5)],
                     [(3, 3), (3, 4), (3, 5), (3, 6)],
                     [(4, 0), (4, 1), (4, 2), (4, 3)],
                     [(4, 1), (4, 2), (4, 3), (4, 4)],
                     [(4, 2), (4, 3), (4, 4), (4, 5)],
                     [(4, 3), (4, 4), (4, 5), (4, 6)],
                     [(5, 0), (5, 1), (5, 2), (5, 3)],
                     [(5, 1), (5, 2), (5, 3), (5, 4)],
                     [(5, 2), (5, 3), (5, 4), (5, 5)],
                     [(5, 3), (5, 4), (5, 5), (5, 6)],
                     [(0, 0), (1, 0), (2, 0), (3, 0)],
                     [(1, 0), (2, 0), (3, 0), (4, 0)],
                     [(2, 0), (3, 0), (4, 0), (5, 0)],
                     [(0, 1), (1, 1), (2, 1), (3, 1)],
                     [(1, 1), (2, 1), (3, 1), (4, 1)],
                     [(2, 1), (3, 1), (4, 1), (5, 1)],
                     [(0, 2), (1, 2), (2, 2), (3, 2)],
                     [(1, 2), (2, 2), (3, 2), (4, 2)],
                     [(2, 2), (3, 2), (4, 2), (5, 2)],
                     [(0, 3), (1, 3), (2, 3), (3, 3)],
                     [(1, 3), (2, 3), (3, 3), (4, 3)],
                     [(2, 3), (3, 3), (4, 3), (5, 3)],
                     [(0, 4), (1, 4), (2, 4), (3, 4)],
                     [(1, 4), (2, 4), (3, 4), (4, 4)],
                     [(2, 4), (3, 4), (4, 4), (5, 4)],
                     [(0, 5), (1, 5), (2, 5), (3, 5)],
                     [(1, 5), (2, 5), (3, 5), (4, 5)],
                     [(2, 5), (3, 5), (4, 5), (5, 5)],
                     [(0, 6), (1, 6), (2, 6), (3, 6)],
                     [(1, 6), (2, 6), (3, 6), (4, 6)],
                     [(2, 6), (3, 6), (4, 6), (5, 6)],
                     [(3, 0), (2, 1), (1, 2), (0, 3)],
                     [(3, 3), (2, 2), (1, 1), (0, 0)],
                     [(4, 0), (3, 1), (2, 2), (1, 3)],
                     [(4, 3), (3, 2), (2, 1), (1, 0)],
                     [(5, 0), (4, 1), (3, 2), (2, 3)],
                     [(5, 3), (4, 2), (3, 1), (2, 0)],
                     [(3, 1), (2, 2), (1, 3), (0, 4)],
                     [(3, 4), (2, 3), (1, 2), (0, 1)],
                     [(4, 1), (3, 2), (2, 3), (1, 4)],
                     [(4, 4), (3, 3), (2, 2), (1, 1)],
                     [(5, 1), (4, 2), (3, 3), (2, 4)],
                     [(5, 4), (4, 3), (3, 2), (2, 1)],
                     [(3, 2), (2, 3), (1, 4), (0, 5)],
                     [(3, 5), (2, 4), (1, 3), (0, 2)],
                     [(4, 2), (3, 3), (2, 4), (1, 5)],
                     [(4, 5), (3, 4), (2, 3), (1, 2)],
                     [(5, 2), (4, 3), (3, 4), (2, 5)],
                     [(5, 5), (4, 4), (3, 3), (2, 2)],
                     [(3, 3), (2, 4), (1, 5), (0, 6)],
                     [(3, 6), (2, 5), (1, 4), (0, 3)],
                     [(4, 3), (3, 4), (2, 5), (1, 6)],
                     [(4, 6), (3, 5), (2, 4), (1, 3)],
                     [(5, 3), (4, 4), (3, 5), (2, 6)],
                     [(5, 6), (4, 5), (3, 4), (2, 3)]]

def get_empty_board():
    return np.zeros((ROWS, COLUMNS))

def get_board_copy(board):
    return np.copy(board)

def get_available_moves(board):
    available_moves = []

    for column in range(COLUMNS):
        if board[0, column] == EMPTY_CELL:
            available_moves.append(column)

    return available_moves

def move(board, player, column):
    new_board = get_board_copy(board)

    empty_row = -1
    for row in range(ROWS):
        if new_board[row, column] != EMPTY_CELL:
            break
        empty_row += 1

    new_board[empty_row, column] = player

    return new_board

def is_board_full(board):
    return len(get_available_moves(board)) == 0

def is_game_over(board):
    return get_winner(board) or is_board_full(board)

def get_cell(board, row, column):
    return board[row, column]

def get_opponent(player):
    return SECOND_PLAYER if player == FIRST_PLAYER else FIRST_PLAYER

def get_winner(board):
    for player in FIRST_PLAYER, SECOND_PLAYER:
        for position in WINNING_POSITIONS:
            is_winning_position = True

            for row, column in position:
                is_player_cell = get_cell(board, row, column) == player
                is_winning_position = is_winning_position and is_player_cell

            if is_winning_position:
                return player

    return None

def display_board(board):
    for row in range(ROWS):
        for column in range(COLUMNS):
            print SYMBOLS[int(board[row, column])] + " ",
        print ""
    print "1  2  3  4  5  6  7"

def get_players():
    human_player = random.choice([FIRST_PLAYER, SECOND_PLAYER])
    return (human_player, SECOND_PLAYER) if human_player == FIRST_PLAYER else (human_player, FIRST_PLAYER)