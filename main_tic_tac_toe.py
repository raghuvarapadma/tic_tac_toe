# main_tic_tac_toe.py

# import all methods from methods.py
from methods import *


def main():
    """
    Function which executes the entire program
    :return: no return value
    """

    print("Welcome to Tic Tac Toe!")

    # creates and displays board to the user
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    display_board(board)

    # while True, both users are playing the game, and once the game ends, while loop breaks
    while True:

        # sets name of player 1 and player 2
        player_dict = {"Player 1": "", "Player 2": ""}
        for i in range(0, 2):
            str_player = input("Player " + str(i+1) + " what would you like your name to be? ")
            player_dict["Player " + str(i+1)] = str_player

        # chooses if player 1 or player 2 gets to select the marker
        player = random.randint(1, 2)

        # this block of code sets X and O equal to player 1 and 2 depending on their preferences
        player_one = ""
        player_two = ""
        if player == 1:
            print(player_dict["Player 1"] + " gets to choose whether they are X or O!")
            player_one = player_input()
            if player_one == "X":
                player_two = "O"
                print(player_dict["Player 1"] + " is X and " + player_dict["Player 2"] + " is O!")
            elif player_one == "O":
                player_two = "X"
                print(player_dict["Player 1"] + " is O and " + player_dict["Player 2"] + " is X!")
        elif player == 2:
            print(player_dict["Player 2"] + " gets to choose whether they are X or O!")
            player_two = player_input()
            if player_two == "X":
                player_one = "O"
                print(player_dict["Player 2"] + " is X and " + player_dict["Player 1"] + " is O!")
            elif player_two == "O":
                player_one = "X"
                print(player_dict["Player 2"] + " is O and " + player_dict["Player 1"] + " is X!")

        # this block of code decides on which player gets to first (cp tracks the turns)
        first_player = choose_first()
        if first_player == "Player 1":
            cp = 1
            print(player_dict["Player 1"] + " gets to go first")
        else:
            cp = 2
            print(player_dict["Player 2"] + " gets to go first")

        # this block of code starts the game
        game = True
        while game:

            # depending on which player goes first, they choose a position, place their marker, and there is a check
            # to see if they have won
            pos = player_choice(board, cp, player_dict)
            if cp % 2 == 1:
                place_marker(board, player_one, pos)
                display_board(board)
                win_c1 = win_check(board, player_one)
                if win_c1:
                    print(player_dict["Player 1"] + " has won!")
                    break
            elif cp % 2 == 0:
                place_marker(board, player_two, pos)
                display_board(board)
                win_c2 = win_check(board, player_two)
                if win_c2:
                    print(player_dict["Player 2"] + " has won!")
                    break

            # if the board has filled up, the game is a tie, or else, the next player goes
            if board_check(board):
                print("The game is a tie!")
                break
            else:
                cp = cp + 1
                continue

        # asks user if they want to replay (breaks loop if "no")
        replay = replay_func()
        if replay:
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            print("The game has restarted!")
        else:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
