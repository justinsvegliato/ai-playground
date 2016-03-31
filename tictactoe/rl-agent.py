import tictactoe
import random

EPSILON = 0.1
INITIAL_WIN_PROBABILITY = 0.5
GAMES = 1000
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

def get_best_move(action_value_map, remaining_moves):
    filtered_action_value_map = get_filtered_action_value_map(action_value_map, remaining_moves)
    best_move = max(filtered_action_value_map, key=filtered_action_value_map.get)
    return best_move.split(MOVE_DELIMITER)

def get_filtered_action_value_map(action_value_map, remaining_moves):
    filtered_action_value_map = {}

    for move in remaining_moves:
        key = get_move_key(move)
        filtered_action_value_map[key] = action_value_map[key]

    return filtered_action_value_map

def get_next_move(action_value_map, remaining_moves):
    return random.choice(remaining_moves) if random.random() <= EPSILON else get_best_move(action_value_map, remaining_moves)

def update_action_value_map(action_value_map, moves, player, winner, games_count):
    for move in moves:
        key = get_move_key(move)

        old_win_probability = action_value_map[key]
        # old_games_count = games_count - 1
        # old_wins_count = old_win_probability * old_games_count

        if winner is None:
            new_win_probability = old_win_probability + 0.5
            # new_win_probability = (old_wins_count + 1) / games_count
        elif player == winner:
            new_win_probability = old_win_probability + 2
            # new_win_probability = (old_wins_count + 1) / games_count
        else:
            new_win_probability = old_win_probability - 2
            # new_win_probability = old_wins_count / games_count

        action_value_map[key] = new_win_probability

def get_move_key(move):
    return str(move[0]) + MOVE_DELIMITER + str(move[1])

def main():
    first_player_action_value_map = get_initial_action_value_map()
    second_player_action_value_map = get_initial_action_value_map()

    first_player_wins = 0
    second_player_wins = 0
    draws = 0

    for i in range(1, GAMES + 1):
        print "Game %d" % (i,)

        (first_player, second_player) = (tictactoe.FIRST_PLAYER, tictactoe.SECOND_PLAYER)

        winner = None
        first_player_moves = []
        second_player_moves = []

        while not tictactoe.is_game_over():
            first_player_move = get_next_move(first_player_action_value_map, tictactoe.get_available_moves())
            first_player_moves.append(first_player_move)

            tictactoe.move(first_player_move[0], first_player_move[1], first_player)

            print "First player: "
            tictactoe.display_board()

            if tictactoe.has_won(first_player):
                winner = first_player
                first_player_wins += 1
                break;

            if tictactoe.is_game_over():
                draws += 1
                break;

            second_player_move = get_next_move(second_player_action_value_map, tictactoe.get_available_moves())
            second_player_moves.append(second_player_move)

            tictactoe.move(second_player_move[0], second_player_move[1], second_player)

            print "Second player: "
            tictactoe.display_board()

            if tictactoe.has_won(second_player):
                winner = second_player
                second_player_wins += 1
                break;

        update_action_value_map(first_player_action_value_map, first_player_moves, first_player, winner, i)
        update_action_value_map(second_player_action_value_map, second_player_moves, second_player, winner, i)

        tictactoe.board = tictactoe.get_initial_board()

    print first_player_action_value_map
    print second_player_action_value_map

    print first_player_wins
    print second_player_wins
    print draws

main()