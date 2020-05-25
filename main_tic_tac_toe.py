# main_tic_tac_toe.py

from methods import *

def main():
    print("Welcome to Tic Tac Toe!")
    board = ["#"] * 9
    display_board(board)

    while True:
        player = random.randint(1,2)
        if (player == 1):
            print("Player 1 gets to choose whether they are X or O!")
            player_one = player_input()
            if (player_one == "X"):
                player_two = "O"
                print("Player 1 is X and Player 2 is O")
            elif (player_one == "O"):
                player_two = "X"
                print("Player 1 is O and Player 2 is X")
        elif (player == 2):
            print("Player 2 gets to choose whether they are X or O!")
            player_two = player_input()
            if (player_two == "X"):
                player_one = "O"
                print("Player 2 is X and Player 1 is O")
            elif (player_two == "O"):
                player_one = "X"
                print("Player 2 is O and Player 1 is X") 
                
        first_Player = choose_first()
        if (first_Player == "Player 1"):
            cP = 1
            print("Player 1 gets to go first")
        else:
            cP = 2
            print("Player 2 gets to go first")
            
        game = True
        while game:
            pos = player_choice(board)
            if (cP % 2 == 1):
                place_marker(board, player_one, pos)
                display_board(board)
                winC1 = win_check(board, player_one)
                if (winC1 == True):
                    print("Player One has won!")
                    break
            elif (cP % 2 == 0):
                place_marker(board, player_two, pos)
                display_board(board)
                winC2 = win_check(board, player_two)
                if (winC2 == True):
                    print("Player Two has won!")
                    break
            if (board_check(board) == True):
                print("The game is a tie!")
                break
            else:
                cP = cP + 1
                continue
                
        replay = replay_func()
        if (replay == True):
            board = ["#"] * 9
            print("The game has restarted!")
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()