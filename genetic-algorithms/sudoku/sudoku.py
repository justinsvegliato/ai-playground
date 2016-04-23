import numpy as np

PUZZLE_SIZE = 9
SQUARE_SIZE = 3

DIGITS = np.array(range(1, PUZZLE_SIZE + 1))

def get_empty_puzzle():
    return np.zeros((PUZZLE_SIZE, PUZZLE_SIZE))

def set_cell(puzzle, row_id, column_id, value):
    new_puzzle = np.copy(puzzle)
    new_puzzle[row_id, column_id] = int(value)
    return new_puzzle

def get_column(puzzle, column_id):
    return puzzle[:, column_id]

def get_row(puzzle, row_id):
    return puzzle[row_id, :]

def get_square(puzzle, square_id):
    start_row_id = (square_id // SQUARE_SIZE) * SQUARE_SIZE
    start_column_id = (square_id % SQUARE_SIZE) * SQUARE_SIZE
    return puzzle[start_row_id:start_row_id + SQUARE_SIZE, start_column_id:start_column_id + SQUARE_SIZE]

def is_row_valid(puzzle, row_id):
    return set(DIGITS) == set(get_row(puzzle, row_id))

def is_column_valid(puzzle, column_id):
    return set(DIGITS) == set(get_column(puzzle, column_id))

def is_square_valid(puzzle, square_id):
    return set(DIGITS) == set(get_square(puzzle, square_id).flatten())

def is_puzzle_valid(puzzle):
    for i in range(PUZZLE_SIZE):
        if not (is_row_valid(puzzle, i) and is_column_valid(puzzle, i) and is_square_valid(puzzle, i)):
            return False
    return True

def load_puzzle(file):
    return np.loadtxt(open(file, "rb"), delimiter=",")

def get_empty_cells(puzzle):
    empty_cells = np.nonzero(puzzle == 0)
    return zip(empty_cells[0], empty_cells[1])

def get_remaining_values(cells):
    return np.setdiff1d(DIGITS, cells)