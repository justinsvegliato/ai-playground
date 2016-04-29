import tictactoe
import minimax_agent
import random

def get_random_phrase(phrases):
    return random.choice(phrases)

def main():
    is_playing = True

    while is_playing:
        human_player, computer_player = tictactoe.get_players()

        turn = 0
        board = tictactoe.get_empty_board()

        print "You're Xs, so you go first!" if human_player == tictactoe.FIRST_PLAYER else "I'm Xs, so you go second!"

        while not tictactoe.is_game_over(board):
            if human_player == tictactoe.FIRST_PLAYER or turn > 0:
                input = raw_input("What's your move? ")
                human_move = input.split(",")
                board = tictactoe.move(board, int(human_move[0]) - 1, int(human_move[1]) - 1, human_player)

                tictactoe.display_board(board)

            if tictactoe.has_won(board, human_player):
                print "You won!"
                break

            if tictactoe.is_game_over(board):
                print "It's a tie!"
                break

            print "I'm thinking..."
            if turn == 0 and computer_player == tictactoe.FIRST_PLAYER:
                computer_move = minimax_agent.get_initial_move()
            else:
                computer_move = minimax_agent.get_best_move(board, computer_player)

            board = tictactoe.move(board, computer_move[0], computer_move[1], computer_player)

            print "I'll play the move (%d, %d)." % (computer_move[0] + 1, computer_move[1] + 1)
            tictactoe.display_board(board)

            if tictactoe.has_won(board, computer_player):
                print "I win!"
                break

            turn += 1

        input = raw_input("Want to play me again? ").lower()
        is_playing = input == "yes" or input == "y"

main()