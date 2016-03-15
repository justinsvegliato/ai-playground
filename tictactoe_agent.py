import numpy as np

FIRST_PLAYER = 1
SECOND_PLAYER = 2

board = np.matrix('0, 0, 0; 0, 0, 0; 0, 0, 0')

def is_valid_move(x, y):
    return board[x, y] == 0

def get_valid_moves():
    return np.nonzero(board == 0)

def move(x, y, player):
    board[x, y] = player