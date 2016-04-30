import connect_four
import minimax_agent

def clear_lines(lines):
    cursor_up_line = '\x1b[1A'
    erase_line = '\x1b[2K'

    for i in range(lines):
        print(cursor_up_line + erase_line + cursor_up_line)

def main():
    is_playing = True

    while is_playing:
        human_player, computer_player = connect_four.get_players()

        turn = 0
        board = connect_four.get_empty_board()

        print "You're red, so you go first!" if human_player == connect_four.FIRST_PLAYER else "I'm red, so I go first!"
        connect_four.display_board(board)

        while not connect_four.get_winner(board):
            if human_player == connect_four.FIRST_PLAYER or turn > 0:
                move = int(raw_input("What's your move? "))
                board = connect_four.move(board, human_player, move - 1)

                clear_lines(9)
                print "You selected column %d." % move
                connect_four.display_board(board)

            if connect_four.get_winner(board):
                break

            print "I'm thinking..."
            computer_move = minimax_agent.get_best_move(board, computer_player)
            board = connect_four.move(board, computer_player, computer_move)

            clear_lines(9)
            print "I'll select column %d." % (computer_move + 1)
            connect_four.display_board(board)
            turn += 1

        print "I win!" if connect_four.get_winner(board) == computer_player else "You win!"

        input = raw_input("Want to play me again? ").lower()
        is_playing = input == "yes" or input == "y"
        clear_lines(10)

main()