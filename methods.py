# methods.py

import random
import re


def display_board(board):
    """
    Displays the board to the user whenever called
    :param board: passes in the board (in the form of an array)
    :return: no return value
    """

    # prints out board to the user
    i = 0
    while i < len(board):
        print("| " + board[i] + " | " + board[i + 1] + " | " + board[i + 2] + "|")
        i = i + 3


def player_input():
    """
    Takes in input from user to track what marker they want
    :return:
    """

    # takes in marker input
    user_marker_choice = ""
    while not (user_marker_choice == "O" or user_marker_choice == "X"):
        user_marker_choice = input("Please select X or O: ")
    return user_marker_choice


def choose_position(cp):
    """
    Asks the user what position they want to place their marker at
    :return: returns user's choice of position
    """

    # goes through while loop to ensure user does not enter in invalid input
    player = ""
    while True:
        try:
            if cp % 2 == 0:
                player = "2"
            elif cp % 2 == 1:
                player = "1"
            user_position_choice = int(input("Player " + player + " please select a position: "))
        except ValueError:
            print("Please enter a valid input!")
            continue
        else:
            print("You entered " + str(user_position_choice) + ".")
            return user_position_choice


def place_marker(board, marker, position):
    """
    Since the board is a array, just assigns the marker to a specific position in the array
    :param board: passes in the board (in the form of an array)
    :param marker: the marker itself (X or O)
    :param position: position marker should be placed at
    :return: no return value
    """

    # when the user enters a position, they are counting one more than the actual position (arrays start at 0)
    board[position - 1] = marker


def win_check(board, marker):
    """
    Checks if there is 3 in a row on the board
    :param board: passes in the board (in the form of an array)
    :param marker: the marker itself (X or O)
    :return: returns True or False depending on if the board contains a match
    """

    if (marker == board[0]) and (marker == board[1]) and (marker == board[2]):
        return True
    elif (marker == board[3]) and (marker == board[4]) and (marker == board[5]):
        return True
    elif (marker == board[6]) and (marker == board[7]) and (marker == board[8]):
        return True
    elif (marker == board[0]) and (marker == board[3]) and (marker == board[6]):
        return True
    elif (marker == board[1]) and (marker == board[4]) and (marker == board[7]):
        return True
    elif (marker == board[2]) and (marker == board[5]) and (marker == board[8]):
        return True
    elif (marker == board[0]) and (marker == board[4]) and (marker == board[8]):
        return True
    elif (marker == board[2]) and (marker == board[4]) and (marker == board[6]):
        return True
    else:
        return False


def choose_first():
    """
    Chooses which players gets to go first
    :return: returns player who goes first
    """

    choose_first_player = random.randint(1, 2)
    if choose_first_player == 1:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, space):
    """
    Checks if space that the user choice is already occupied
    :param board: passes in the board (in the form of an array)
    :param space: specific position that needs to be checked (x-1 since board in format of an array)
    :return: either returns True or False depending on if space is available
    """

    if re.search("\d", board[space - 1]):
        return True
    else:
        print("Can't place your marker here!")
        return False


def board_check(board):
    """
    Checks if the game is currently a tie (sees if board is filled)
    :param board: passes in the board (in the form of an array)
    :return: either returns True or False depending on if the board is filled
    """

    i = 0
    while i < len(board):
        if (board[i] == "X") or (board[i] == "O"):
            i = i + 1
            continue
        else:
            return False

    return True


def player_choice(board, cp):
    """
    Asks the player where they would like to place their marker on the board
    :param cp: variable which keeps track of player's turn
    :param board: asses in the board (in the form of an array)
    :return: returns the position they would like to place their marker
    """

    position = 0
    pos_available = False
    while not pos_available:
        while True:
            position = choose_position(cp)
            if position not in range(1, 10):
                print("Please enter in a position from 1 through 9!")
                continue
            else:
                break
        pos_available = space_check(board, position)

        if pos_available:
            break
        else:
            continue
    return position


def replay_func():
    """
    Determines whether players want to play again
    :return: either returns True or False depending on if users want to play again
    """
    while True:
        try:
            response = input("Do you want to play again? ")
        except ValueError:
            print("Please enter a valid response!")
        else:
            if response.lower() == "yes":
                return True
            elif response.lower() == "no":
                return False
            else:
                print("Please enter a valid response!")
                continue
