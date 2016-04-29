import sudoku
import random
import sys

POPULATION_SIZE = 300
GENERATIONS = 100000
ELITE_MEMBER_COUNT = 5
MUTATION_LIMIT = 15

def get_fitness_score(puzzle):
    fitness_score = 0

    for i in range(sudoku.PUZZLE_SIZE):
        if sudoku.is_column_valid(puzzle, i):
            fitness_score += 1

        if sudoku.is_row_valid(puzzle, i):
            fitness_score += 1

        if sudoku.is_square_valid(puzzle, i):
            fitness_score += 1

    return fitness_score

def get_initial_population(initial_puzzle, capacity):
    population = []

    for puzzle_id in range(capacity):
        puzzle = initial_puzzle
        for row_id, column_id in sudoku.get_empty_cells(initial_puzzle):
            value = get_cell_value(puzzle, row_id, column_id)
            puzzle = sudoku.set_cell(puzzle, row_id, column_id, value)

        population.append(puzzle)

    return population

def get_cell_value(puzzle, row_id, column_id):
    if random.random() < 0.2:
        return random.choice(sudoku.DIGITS)

    cells = sudoku.get_column(puzzle, column_id) if random.random() > 0.5 else sudoku.get_row(puzzle, row_id)
    values = sudoku.get_remaining_values(cells)

    return random.choice(values) if len(values) > 0 else random.choice(sudoku.DIGITS)

def get_enriched_population(population):
    enriched_population = []

    for puzzle_id in range(len(population)):
        puzzle = population[puzzle_id]
        fitness = get_fitness_score(puzzle)
        enriched_population.append([puzzle, fitness])

    return enriched_population

def get_elite_members(population, capacity):
    enriched_population = get_enriched_population(population)
    sorted_population = sorted(enriched_population, key=lambda x: x[1], reverse=True)
    raw_population = [puzzle[0] for puzzle in sorted_population]
    return raw_population[:capacity]

def get_mutated_puzzle(initial_puzzle, puzzle):
    empty_cells = sudoku.get_empty_cells(initial_puzzle)

    mutations = random.choice(range(MUTATION_LIMIT)) + 1

    mutated_puzzle = puzzle
    for mutation in range(mutations):
        empty_cell = random.choice(empty_cells)
        value = get_cell_value(puzzle, empty_cell[0], empty_cell[1])
        mutated_puzzle = sudoku.set_cell(mutated_puzzle, empty_cell[0], empty_cell[1], value)

    return mutated_puzzle

def get_average_fitness_score(population):
    fitness_score_sum = 0

    for i in range(len(population)):
        fitness_score_sum += get_fitness_score(population[i])

    return fitness_score_sum / len(population)

def get_highest_fitness_score(population):
    enriched_population = get_enriched_population(population)
    return max(enriched_population, key=lambda x:x[1])[1]

def main():
    if len(sys.argv) < 2:
        print "Usage: python minimax_agent.py file"
        sys.exit()

    initial_puzzle = sudoku.load_puzzle(sys.argv[1])
    population = get_initial_population(initial_puzzle, POPULATION_SIZE)

    for generation in range(GENERATIONS):
        if sudoku.is_puzzle_valid(population[0]):
            break

        new_population = get_elite_members(population, ELITE_MEMBER_COUNT)
        for i in range(POPULATION_SIZE - ELITE_MEMBER_COUNT):
            puzzle = random.choice(population)
            mutated_puzzle = get_mutated_puzzle(initial_puzzle, puzzle)
            new_population.append(mutated_puzzle)
        population = new_population

        print "Generation %d's Fitness Score: %d" % (generation, get_highest_fitness_score(population))

    print "Best Solution:"
    print population[0]

main()