import tictactoe
import random

EPSILON = 0.1
INITIAL_WIN_PROBABILITY = 0.5
GAME_COUNT = 1000
MOVE_DELIMITER = ","

def get_initial_action_value_map():
    return {
        "0,0": INITIAL_WIN_PROBABILITY,
        "0,1": INITIAL_WIN_PROBABILITY,
        "0,2": INITIAL_WIN_PROBABILITY,
        "1,0": INITIAL_WIN_PROBABILITY,
        "1,1": INITIAL_WIN_PROBABILITY,
        "1,2": INITIAL_WIN_PROBABILITY,
        "2,0": INITIAL_WIN_PROBABILITY,
        "2,1": INITIAL_WIN_PROBABILITY,
        "2,2": INITIAL_WIN_PROBABILITY
    }

def get_best_move(action_value_map, available_moves):
    available_action_value_map = get_available_action_value_map(action_value_map, available_moves)
    best_move = max(available_action_value_map, key=available_action_value_map.get)
    return best_move.split(MOVE_DELIMITER)

def get_available_action_value_map(action_value_map, available_moves):
    available_action_value_map = {}

    for move in available_moves:
        key = get_move_key(move)
        available_action_value_map[key] = action_value_map[key]

    return available_action_value_map

def get_next_move(action_value_map, remaining_moves):
    return random.choice(remaining_moves) if random.random() <= EPSILON else get_best_move(action_value_map, remaining_moves)

def get_reward(winner, player):
    if winner is None:
        return 1

    if winner == player:
        return 2

    return 0

def update_action_value_map(action_value_map, moves, player, winner, games_count):
    for move in moves:
        key = get_move_key(move)

        old_wins_count = action_value_map[key] * (games_count - 1)
        reward = get_reward(winner, player)

        action_value_map[key] = (old_wins_count + reward) / games_count

def get_move_key(move):
    return str(move[0]) + MOVE_DELIMITER + str(move[1])

def train():
    first_player_action_value_map = get_initial_action_value_map()
    second_player_action_value_map = get_initial_action_value_map()

    first_player_win_count = 0
    second_player_win_count = 0
    draw_count = 0

    for i in range(1, GAME_COUNT + 1):
        print "Game " + str(i)

        (first_player, second_player) = (tictactoe.FIRST_PLAYER, tictactoe.SECOND_PLAYER)
        first_player_moves = []
        second_player_moves = []

        winner = None
        board = tictactoe.get_empty_board()

        while not tictactoe.is_game_over(board):
            first_player_move = get_next_move(first_player_action_value_map, tictactoe.get_available_moves(board))
            first_player_moves.append(first_player_move)

            tictactoe.move(board, first_player_move[0], first_player_move[1], first_player)

            print "First Player: "
            tictactoe.display_board(board)

            if tictactoe.has_won(board, first_player):
                winner = first_player
                first_player_win_count += 1
                break;

            if tictactoe.is_game_over(board):
                draw_count += 1
                break;

            second_player_move = get_next_move(second_player_action_value_map, tictactoe.get_available_moves(board))
            second_player_moves.append(second_player_move)

            tictactoe.move(board, second_player_move[0], second_player_move[1], second_player)

            print "Second Player: "
            tictactoe.display_board(board)

            if tictactoe.has_won(board, second_player):
                winner = second_player
                second_player_win_count += 1
                break;

        update_action_value_map(first_player_action_value_map, first_player_moves, first_player, winner, i)
        update_action_value_map(second_player_action_value_map, second_player_moves, second_player, winner, i)

    print "Summary: "
    print "First Player Action-Value Map: " + str(first_player_action_value_map)
    print "Second Player Action-Value Map: " + str(second_player_action_value_map)
    print "First Player Wins: " + str(first_player_win_count)
    print "Second Player Wins: " + str(second_player_win_count)
    print "Draws: " + str(draw_count)

    return first_player_action_value_map, second_player_action_value_map