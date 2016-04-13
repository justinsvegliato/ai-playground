import numpy as np

PUZZLE_SIZE = 9

DIGITS = np.array(range(1, PUZZLE_SIZE + 1))

def get_empty_puzzle():
    return np.zeros((PUZZLE_SIZE, PUZZLE_SIZE))

def set_cell(puzzle, row_id, column_id, value):
    puzzle[row_id, column_id] = int(value)

def get_column(puzzle, column_id):
    return puzzle[:, column_id]

def get_row(puzzle, row_id):
    return puzzle[row_id, :]

def is_row_valid(puzzle, row_id):
    return set(DIGITS) == set(get_row(puzzle, row_id))

def is_column_valid(puzzle, column_id):
    return set(DIGITS) == set(get_column(puzzle, column_id))

def is_square_valid(puzzle, square_id):
    pass

p = get_empty_puzzle()
set_cell(p, 0, 0, 9)
set_cell(p, 1, 0, 8)
set_cell(p, 2, 0, 7)
set_cell(p, 3, 0, 6)
set_cell(p, 4, 0, 5)
set_cell(p, 5, 0, 4)
set_cell(p, 6, 0, 3)
set_cell(p, 7, 0, 2)
set_cell(p, 8, 0, 1)

print is_row_valid(p, 0)
print is_column_valid(p, 0)
print p