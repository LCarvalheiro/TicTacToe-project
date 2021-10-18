def player_turns():
    print("Player 1 Turn!(X)\n")
    turn = 'X'

    game_board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                  'B1': ' ', 'B2': ' ', 'B3': ' ',
                  'C1': ' ', 'C2': ' ', 'C3': ' '}

    count = 0
    for i in range(10):

        draw_game_board(game_board)
        move = input("Choose coordinates to place token: ").upper()

        while not validate_move(move):
            print("Not valid please choose another coordinate:")
            move = input().upper()

        if game_board[move] == ' ':
            game_board[move] = turn
            count += 1
        else:
            print("Place already in use , choose another:")
            continue

        if count >= 5:

            if (game_board['A1'] == game_board['A2'] == game_board['A3'] != ' ') \
                    or (game_board['B1'] == game_board['B2'] == game_board['B3'] != ' ') \
                    or (game_board['C1'] == game_board['C2'] == game_board['C3'] != ' ') \
                    or (game_board['A1'] == game_board['B1'] == game_board['C1'] != ' ') \
                    or (game_board['A2'] == game_board['B2'] == game_board['C2'] != ' ') \
                    or (game_board['A3'] == game_board['B3'] == game_board['C3'] != ' ') \
                    or (game_board['A1'] == game_board["B2"] == game_board['C3'] != ' ') \
                    or (game_board['A3'] == game_board["B2"] == game_board['C1'] != ' '):

                draw_game_board(game_board)
                if turn == 'X':
                    print("Player 1 Won!")
                else:
                    print("Player 2 Won!")
                break

        if count == 9:
            print("Draw!!!")
            break

        if turn == 'X':
            print("Payer 2 turn!(O)")
            turn = 'O'
        else:
            print("Player 1 turn! (X)")
            turn = 'X'


def draw_game_board(game_board):
    print("  1  2  3\n  --------")
    print("A " + game_board['A1'] + ' |' + game_board['A2'] + ' |' + game_board['A3'])
    print('  --------')
    print('B ' + game_board['B1'] + ' |' + game_board['B2'] + ' |' + game_board['B3'])
    print('  --------')
    print('C ' + game_board['C1'] + ' |' + game_board['C2'] + ' |' + game_board['C3'])


def validate_move(move):
    if (move[0] == 'A' or move[0] == 'B' or move[0] == 'C') and (move[1] == '1' or move[1] == '2' or move[1] == '3'):
        return True


def play_game():
    print("\nWELCOME TO TIC TAC TOE\n")

    player_turns()
    if replay() is True:
        play_game()


def replay():
    choice = input("Play again? Enter Yes or No: ")
    while choice not in ['Yes', 'No']:
        choice = input("Play again? Enter Yes or No: ")

    return choice == 'Yes'


# player_turns()
play_game()
