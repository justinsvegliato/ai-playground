import numpy as np
import random

EMPTY_SQUARE = 0
FIRST_PLAYER = 1
SECOND_PLAYER = 2

DISPLAY_MAP = {}
DISPLAY_MAP[FIRST_PLAYER] = "X"
DISPLAY_MAP[SECOND_PLAYER] = "O"
DISPLAY_MAP[EMPTY_SQUARE] = "-"

def get_initial_board():
    return np.matrix("0, 0, 0; 0, 0, 0; 0, 0, 0")

def move(x, y, player):
    board[x, y] = player

def is_valid_move(x, y):
    return board[x, y] == EMPTY_SQUARE

def get_available_moves():
    size = get_board_size()
    moves = []

    for x in range(size):
        for y in range(size):
            if board[x, y] == EMPTY_SQUARE:
                moves.append([x, y])

    return moves

def is_board_full():
    return len(get_available_moves()) == 0

def has_won(player):
    size = get_board_size()

    for i in range(size):
        if np.all(board[i] == player) or np.all(board[:, i] == player):
            return True

    return np.all(np.diagonal(board) == player) or np.all(np.diagonal(np.fliplr(board)) == player)

def get_winner():
    return FIRST_PLAYER if has_won(FIRST_PLAYER) else SECOND_PLAYER

def is_game_over():
    return has_won(FIRST_PLAYER) or has_won(SECOND_PLAYER) or is_board_full()

def get_board_size():
    return len(board)

def display_board():
    size = get_board_size()

    for x in range(size):
        for y in range(size):
            print DISPLAY_MAP[board[x, y]],
        print ""

def get_players():
    human_player = random.choice([FIRST_PLAYER, SECOND_PLAYER])
    return (human_player, SECOND_PLAYER) if human_player == FIRST_PLAYER else (human_player, FIRST_PLAYER)

def play():
    (human_player, computer_player) = get_players()
    turn = 0

    print "You're X's, so you go first." if human_player == FIRST_PLAYER else "The computer is X's, so you go second."

    while not is_game_over():
        if human_player == FIRST_PLAYER or turn > 0:
            input = raw_input("Make a move: ")
            human_move = input.split(",")
            move(human_move[0], human_move[1], human_player)
            display_board()

        if has_won(human_player):
            print "You won!"
            break;

        computer_move = random.choice(get_available_moves())
        move(computer_move[0], computer_move[1], computer_player)
        print "The computer has moved: %d, %d" % (computer_move[0], computer_move[1])
        display_board()

        if has_won(computer_player):
            print "The computer has won!"
            break;

        turn += 1

board = get_initial_board()