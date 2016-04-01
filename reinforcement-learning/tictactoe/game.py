import tictactoe
import smart_agent

def main():
    print "The computer is learning how to play! Please wait a moment."
    (first_player_action_value_map, second_player_action_value_map) = smart_agent.train()

    is_playing = True

    while is_playing:
        (human_player, computer_player) = tictactoe.get_players()
        computer_action_value_map = second_player_action_value_map if human_player == tictactoe.FIRST_PLAYER else first_player_action_value_map

        turn = 0
        board = tictactoe.get_empty_board()

        print "You're X's, so you go first." if human_player == tictactoe.FIRST_PLAYER else "The computer is X's, so you go second."

        while not tictactoe.is_game_over(board):
            if human_player == tictactoe.FIRST_PLAYER or turn > 0:
                input = raw_input("Make a move: ")
                human_move = input.split(",")
                tictactoe.move(board, human_move[0], human_move[1], human_player)

                tictactoe.display_board(board)

            if tictactoe.has_won(board, human_player):
                print "You won!"
                break;

            if tictactoe.is_game_over(board):
                print "There was a draw!"
                break;

            computer_move = smart_agent.get_best_move(computer_action_value_map, board, computer_player, tictactoe.get_available_moves(board))
            tictactoe.move(board, computer_move[0], computer_move[1], computer_player)

            print "The computer has moved: %s, %s" % (computer_move[0], computer_move[1])
            tictactoe.display_board(board)

            if tictactoe.has_won(board, computer_player):
                print "The computer has won!"
                break;

            turn += 1

        input = raw_input("Want to play again? ")
        is_playing = input == "Yes" or input == "yes" or input == "y"

main()