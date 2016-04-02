import tictactoe
import random
import itertools

EPSILON = 0.2
INITIAL_WIN_PROBABILITY = 0.5
GAME_COUNT = 10000

def get_best_move(state_value_map, board, player, available_moves):
    best_move = None
    best_move_value = -1000000000

    random.shuffle(available_moves)

    for move in available_moves:
        board_copy = tictactoe.get_board_copy(board)
        tictactoe.move(board_copy, move[0], move[1], player)

        key = tictactoe.get_string_representation(board_copy)

        if state_value_map[key] > best_move_value:
            best_move = move
            best_move_value = state_value_map[key]

    return best_move

def get_next_move(state_value_map, board, player, available_moves):
    return random.choice(available_moves) if random.random() <= EPSILON else get_best_move(state_value_map, board, player, available_moves)

def get_reward(winner, player):
    if winner is None:
        return 0

    if winner == player:
        return 1

    return -1

    # This is the old reward calculation:
    # return 1 if winner == player else 0

def update_state_value_map(state_value_map, boards, player, winner, game_count):
    for board in boards:
        key = tictactoe.get_string_representation(board)

        state_value_map[key] += get_reward(winner, player)

        # This is the old value calculation:
        # old_win_count = state_value_map[key] * (game_count - 1)
        # reward = get_reward(winner, player)
        #
        # state_value_map[key] = (old_win_count + reward) / game_count

def get_initial_state_value_map():
    state_value_map = {}

    for permutation in itertools.product([0, 1, 2], repeat=9):
        key = ''.join(map(str, permutation))

        state_value_map[key] = 0

        # This is the old default value:
        # state_value_map[key] = INITIAL_WIN_PROBABILITY

    return state_value_map

def train():
    first_player_state_value_map = get_initial_state_value_map()
    second_player_state_value_map = get_initial_state_value_map()

    first_player_win_count = 0
    second_player_win_count = 0
    draw_count = 0

    for i in range(1, GAME_COUNT + 1):
        print "Playing game " + str(i) + "..."

        (first_player, second_player) = (tictactoe.FIRST_PLAYER, tictactoe.SECOND_PLAYER)
        first_player_boards = []
        second_player_boards = []

        winner = None
        board = tictactoe.get_empty_board()

        while not tictactoe.is_game_over(board):
            first_player_move = get_next_move(first_player_state_value_map, board, first_player, tictactoe.get_available_moves(board))
            tictactoe.move(board, first_player_move[0], first_player_move[1], first_player)
            first_player_boards.append(board)

            if tictactoe.has_won(board, first_player):
                winner = first_player
                first_player_win_count += 1
                break;

            if tictactoe.is_game_over(board):
                draw_count += 1
                break;

            second_player_move = get_next_move(second_player_state_value_map, board, second_player, tictactoe.get_available_moves(board))
            tictactoe.move(board, second_player_move[0], second_player_move[1], second_player)
            second_player_boards.append(board)

            if tictactoe.has_won(board, second_player):
                winner = second_player
                second_player_win_count += 1
                break;

            if tictactoe.is_game_over(board):
                draw_count += 1
                break;

        update_state_value_map(first_player_state_value_map, first_player_boards, first_player, winner, i)
        update_state_value_map(second_player_state_value_map, second_player_boards, second_player, winner, i)

    print "Summary: "
    print "First Player Wins: " + str(first_player_win_count)
    print "Second Player Wins: " + str(second_player_win_count)
    print "Draws: " + str(draw_count)

    return first_player_state_value_map, second_player_state_value_map