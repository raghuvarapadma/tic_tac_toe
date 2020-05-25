# methods.py

import random

def display_board(board):
    i = 0
    while i < len(board):
        print ("| " + board[i] + " | " + board[i+1] + " | " + board[i+2] + "|")
        i = i + 3

def player_input():
    pInput = ""
    while (not(pInput == "O" or pInput == "X")):
        pInput = input("Please select X or O: ")
    return pInput

def choose_position():
    while True:
        try:
            pValue = int(input("Please select a position: "))
        except TypeError:
            print("Please enter a valid input!")
            continue
        else:
            print("You entered " + str(pValue) + ".")
            return pValue
            break

def place_marker(board, marker, position):
    board[position-1] = marker

def win_check(board, marker):
    if ((marker == board[0]) and (marker == board[1]) and (marker == board[2])):
        return True
    elif ((marker == board[3]) and (marker == board[4]) and (marker == board[5])):
        return True
    elif ((marker == board[6]) and (marker == board[7]) and (marker == board[8])):
        return True
    elif ((marker == board[0]) and (marker == board [3]) and (marker == board[6])):
        return True
    elif ((marker == board[1]) and (marker == board [4]) and (marker == board[7])):
        return True
    elif ((marker == board[2]) and (marker == board [5]) and (marker == board[8])):
        return True
    elif ((marker == board[0]) and (marker == board [4]) and (marker == board[8])):
        return True
    elif ((marker == board[2]) and (marker == board [4]) and (marker == board[6])):
        return True
    else:
        return False

def choose_first():
    chooseFirstVar = random.randint(1,2)
    if (chooseFirstVar == 1):
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, space):
    if (board[space-1] == "#"):
        return True
    else:
        print("Can't place your marker here!")
        return False

def board_check(board):
    i = 0
    sum_board = 0
    retVal = True
    while i < len(board):
        if ((board[i] == "X") or (board[i] == "O")):
            sum_board += 1
        else:
            pass
        i = i + 1
    if (i == sum_board):
        return True
    else:
        return False

def player_choice(board):
    position = 0
    retVal = False
    while (retVal == False):
        position = choose_position()
        retVal = space_check(board, position)
        if (retVal == True):
            break
        else:
            continue
    return position

def replay_func():
    while True:
        try:
            response = input("Do you want to play again? ")
        except TypeError:
            print("Please enter a valid response!")
        else:
            if (response.lower() == "yes"):
                return True
                break
            elif (response.lower() == "no"):
                return False
                break
            else:
                print("Please enter a valid response!")
                continue