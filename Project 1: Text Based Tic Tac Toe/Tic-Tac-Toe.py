'''
 Text Based 2-Player Tic Tac Toe Game
 '''

import random

''' Tic Tac Toe Game Structure '''
# Step 1 -: Create a function that would list the instructions of the game
# Step 2 -: Create a function that would display the board
# Step 3 -: Create a function to allow players to choose between X and O
# Step 4 -: Create a game environment that continues to play the game until there's a winner or all spaces are filled
# Step 5 -: Create a function or logic flow with data validation that allows players to make moves on the board
# Step 6 -: Create a function or conditional logic that checks win for X or O
# Step 7 -: If there is a winner display the player who won the game
# Step 8 -: Ask if the user wants to play game. If yes, repeat the game from the beginning, else, end the game.

def instructions():
    # A function that would list the instructions of the game

    print('Tic Tac Toe \n')
    print('How to play: ')
    print('1.) Both players will choose whether to be "X" or "O" ')
    print('2.) To even the odds of winning, players will be randomly chosen to start ')
    print('3. On the board, players can choose the position with numbers from 1-9')
    print('3.) The first player to achieve a straight, horizontal, or vertical wins the game')
    print('4.) If players want to play again, press "Y" at the end of each game, or press "N" to end the game \n')

    print('Each position on the board is based on a numerical position from 1-9 \n')
    print(f' {1}  |  {2}  |  {3} ')
    print('---------------')
    print(f' {4}  |  {5}  |  {6} ')
    print('---------------')
    print(f' {7}  |  {8}  |  {9} ')
    print('')

def display_board(list):
    # A function that displays the board after each move

    print(list[0],' | ',list[1],' | ',list[2])
    print('---------------')
    print(list[3],' | ',list[4],' | ',list[5])
    print('---------------')
    print(list[6],' | ', list[7],' | ',list[8])
    print('')

def player_choice():
    # A function that allows players to choose between X and O with data validation

    while True:
        player1 = input('Please choose between "X" or "O": ').upper()
        print("")

        if player1.upper() == "X" or player1.upper() == "O":
            print(f'Player 1 is {player1}')
            break

        else:
            print('Invalid entry. Please choose between "X" and "O" ')
            print("")

    return player1


def check_winner(list):
    ''' Checks for winners for X and O '''

    # Diagonal Checks for X
    if list[0].upper() == 'X' and list[4].upper() == 'X' and list[8].upper() == 'X':
        return 'X has won'

    elif list[2].upper() == 'X' and list[4].upper() == 'X' and list[6].upper() == 'X':
        return 'X has won'

    # Vertical Checks for X

    elif list[0].upper() == 'X' and list[3].upper() == 'X' and list[6].upper() == 'X':
        return 'X has won'

    elif list[1].upper() == 'X' and list[4].upper() == 'X' and list[7].upper() == 'X':
        return 'X has won'


    elif list[2].upper() == 'X' and list[5].upper() == 'X' and list[8].upper() == 'X':
        return 'X has won'


    # Horizontal Checks for X

    elif list[0].upper() == 'X' and list[1].upper() == 'X' and list[2].upper() == 'X':
        return 'X has won'


    elif list[3].upper() == 'X' and list[4].upper() == 'X' and list[5].upper() == 'X':
        return 'X has won'

    elif list[6].upper() == 'X' and list[7].upper() == 'X' and list[8].upper() == 'X':
        return 'X has won'

    ''' Check for O wins '''

    # Diagonal Checks for O
    if list[0].upper() == 'O' and list[4].upper() == 'O' and list[8].upper() == 'O':
        return 'O has won'

    elif list[2].upper() == 'O' and list[4].upper() == 'O' and list[6].upper() == 'O':
        return 'O has won'


    # Vertical Checks for O

    elif list[0].upper() == 'O' and list[3].upper() == 'O' and list[6].upper() == 'O':
        return 'O has won'

    elif list[1].upper() == 'O' and list[4].upper() == 'O' and list[7].upper() == 'O':
        return 'O has won'

    elif list[2].upper() == 'O' and list[5].upper() == 'O' and list[8].upper() == 'O':
        return 'O has won'


    # Horizontal Checks for O

    elif list[0].upper() == 'O' and list[1].upper() == 'O' and list[2].upper() == 'O':
        return 'O has won'

    elif list[3].upper() == 'O' and list[4].upper() == 'O' and list[5].upper() == 'O':
        return 'O has won'

    elif list[6].upper() == 'O' and list[7].upper() == 'O' and list[8].upper() == 'O':
        return 'O has won'


def play_game():
    # A function with logic flow and data validation that allows players to make moves on the board

    moves_list = ['','','','','','','','','']
    move_range = [1,2,3,4,5,6,7,8,9]
    player1 = player_choice()

    if player1.upper() == 'X':
        player2 = 'O'
        print(f'Player 2 is {player2}\n')

    elif player1.upper() == 'O':
        player2 = 'X'
        print(f'Player 2 is {player2}\n')

    move_count = 0

    player_select = [player1,player2]
    random.shuffle(player_select)

    if player_select[0].upper() == player1:
        print(f'Player 1 ({player1}) to start\n')

    elif player_select[0].upper() == player2:
        print(f'Player 2 ({player2}) to start\n')

    display_board(moves_list)

    game_over = ''

    # Start the Game
    while move_count != 9:

        while True:
            # Player 1 / First Move
            player_move = input(f'({player_select[0]}) Please enter a position on the board (1-9): ')
            print('')

            if player_move.isdigit() == True:

                player_move = int(player_move)

                if player_move in move_range and moves_list[player_move - 1] == '':
                    moves_list[player_move-1] = player_select[0]
                    display_board(moves_list)
                    move_count += 1
                    game_over = check_winner(moves_list)
                    break

                elif player_move in move_range and moves_list[player_move - 1] != '':
                    # Stops players from choosing the same position
                    print('This position is already taken. Please try again.\n')
                    continue

                else:
                    print('Please choose a position between 1-9 \n')
                    continue

            else:
                print('That is an invalid entry. Please try again \n')
                continue


        if str(game_over) == f'{player_select[0]} has won':
            print(game_over + '\n')
            move_count = 9
            break

        elif game_over == f'{player_select[0]} has won' and move_count == 9:
            print("It's a draw \n")

        while move_count != 9:
            # Player 2 / Second Move
            game_over = str(check_winner(moves_list))


            player_move = input(f'({player_select[1]}) Please enter a position on the board (1-9): ')
            print('')

            if player_move.isdigit() == True:
                player_move = int(player_move)


                if player_move in move_range and moves_list[player_move - 1] == '':
                    moves_list[player_move-1] = player_select[1]
                    display_board(moves_list)
                    move_count += 1
                    game_over = check_winner(moves_list)
                    break

                elif game_over == f'{player2} has won':
                    move_count = 9
                    break

                elif player_move in move_range and moves_list[player_move - 1] != '':
                    # Stops players from choosing the same position
                    print('This position is already taken. Please try again.\n')
                    continue

                else:
                    print('Please choose a position between 1-9 \n')
                    continue

            else:
                print('That is an invalid entry. Please try again \n')
                continue

        if str(game_over) == f'{player_select[1]} has won':
            print(game_over + '\n')
            move_count = 9
            break

        elif game_over != f'{player_select[1]} has won' and move_count == 9:
            print("It's a draw \n")


# Start the Official Game of Tic Tac Toe

instructions()

start_game = True

while start_game:
    play_game()

    while True:
        reset_game = input('Press "Y" to play again or Press "N" to end the game: ')
        print('')

        if reset_game.upper() == 'Y':
            break

        elif reset_game.upper() == 'N':
            print('Thank you for playing!!!')
            start_game = False
            break

        else:
            print('Invalid Entry. Please try again \n')

