# This is a text-based tic tac toe game where two players will play against each other to win.

import numpy as np

print("-( TIC TAC TOE )-")

PLAYER_A = 'X'
PLAYER_B = 'O'

running = True
valid = False
turn_count = 0
player = PLAYER_B
board = [['-','-','-'], ['-','-','-'], ['-','-','-']]


def update_board(board_array):
    temp_board = '-------\n'

    for y in board_array:
        temp_board += '|'
        for x in y:
            temp_board += f'{x}|'
        temp_board += '\n-------\n'

    return temp_board


def check_player(turn_count):
    global player
    if turn_count % 2 == 0:
        player = PLAYER_A
    else:
        player = PLAYER_B


def get_position(input_text):
    global valid
    position = []
    for word in input_text.split():
        if word.isdigit() and len(position) < 2:
            position.append(int(word) - 1)

            if int(word) > 3 or int(word) < 1:
                print("number has to be between 1 and 3")
                break
            else:
                valid = True

        elif len(position) >= 2:
            break;

    if len(position) != 2:
        print("please input only two numbers")
        valid = False
    return position


def place_x(position):
    board[position[1]][position[0]] = PLAYER_A


def place_o(position):
    board[position[1]][position[0]] = PLAYER_B


def valid_position(position):
    return board[position[1]][position[0]] == '-'


def check_victory(board_array):
    victory = False
    _board_N = np.array(board_array)
    _board_T = np.array(board_array).T

    for i in range(_board_N.shape[0]):
        if np.all(_board_N[i] == _board_N[i][0]) and (_board_N[i][0] == PLAYER_A or _board_N[i][0]  == PLAYER_B):
            victory = True
            break

    for i in range(_board_T.shape[0]):
        if np.all(_board_T[i] == _board_T[i][0]) and (_board_T[i][0] == PLAYER_A or _board_T[i][0]  == PLAYER_B):
            victory = True
            break

    if _board_N[0][0] == _board_N[1][1] == _board_N[2][2] and (_board_N[0][0] == PLAYER_A or _board_N[0][0] == PLAYER_B):
        victory = True

    if _board_T[0][0] == _board_T[1][1] == _board_T[2][2] and (_board_T[0][0] == PLAYER_A or _board_T[0][0] == PLAYER_B):
        victory = True

    return victory


while running:
    turn_count += 1
    valid = False
    check_player(turn_count)
    print(f"Turn: {turn_count}")
    print(f"{player}'s turn")

    new_board = update_board(board)
    print(new_board)

    while not valid:
        get_order = input('INPUT: ')
        pos = get_position(get_order)
        if not valid_position(pos):
            print('Position is not valid')
            valid = False
        print(pos)

    if valid:
        if player == PLAYER_A:
            place_x(pos)
        elif player == PLAYER_B:
            place_o(pos)

    if check_victory(board):
        print(f"{player} is the victor!")
        break;
