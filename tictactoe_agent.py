import numpy as np
import random

EMPTY_SQUARE = 0
FIRST_PLAYER = 1
SECOND_PLAYER = 2

DISPLAY_MAP = {}
DISPLAY_MAP[FIRST_PLAYER] = "X"
DISPLAY_MAP[SECOND_PLAYER] = "O"
DISPLAY_MAP[EMPTY_SQUARE] = "-"

board = np.matrix("0, 0, 0; 0, 0, 0; 0, 0, 0")
size = len(board)

def display_board():
    for x in range(size):
        for y in range(size):
            print DISPLAY_MAP[board[x, y]],
        print ""

def is_valid_move(x, y):
    return board[x, y] == EMPTY_SQUARE

def get_available_moves():
    moves = []

    for x in range(size):
        for y in range(size):
            if board[x, y] == EMPTY_SQUARE:
                moves.append([x, y])

    return moves

def is_board_full():
    return len(get_available_moves()) == 0

def move(x, y, player):
    board[x, y] = player

def is_game_over():
    return has_won(FIRST_PLAYER) or has_won(SECOND_PLAYER) or is_board_full()

def has_won(player):
    for i in range(size):
        if np.all(board[i] == player) or np.all(board[:, i] == player):
            return True

    return np.all(np.diagonal(board) == player) or np.all(np.diagonal(np.fliplr(board)) == player)

def __main__():
    player = random.choice([FIRST_PLAYER, SECOND_PLAYER])
    turn = 0

    print "You're X's, so you go first." if player == FIRST_PLAYER else "You're O's, so you go second."

    while not is_game_over():
        if player == FIRST_PLAYER or turn > 0:
            input = raw_input("Make a move: ")
            coordinates = input.split(",")
            move(coordinates[0], coordinates[1], FIRST_PLAYER)
            display_board()

        computer_move = random.choice(get_available_moves())
        move(computer_move[0], computer_move[1], SECOND_PLAYER)

        print "The computer has moved: %d, %d" % (computer_move[0], computer_move[1])
        display_board()

        turn += 1

__main__()