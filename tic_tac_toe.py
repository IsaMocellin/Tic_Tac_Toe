# Seção: Loop principal do jogo

import sys
sys.path.append('Projeto Jogo da Velha\Modulos')

from player_input import player_input
from choose_first import choose_first
from display_board import display_board
from place_marker import place_marker
from win_check import win_check
from space_check import space_check
from full_board_check import full_board_check
from player_choice import player_choice
from replay import replay

print(' ─────────────────────────')
print('┃ Welcome to Tic Tac Toe! ┃')
print(' ─────────────────────────')

while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print('')
    print(turn + ' will go first.')
    
    print('')
    play_game = input('Ready to play? (y/n) ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':
            print('')
            display_board(the_board)
            print('')
            print('« PLAYER 1 TURN »')
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('')
                print('✧ Player 1 has WON ✧')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('')
                    print('∵ TIE GAME! ∴')
                    game_on = False
                else:
                    turn = 'Player 2'
        if turn == 'Player 2':
            print('')
            display_board(the_board)
            print('')
            print('« PLAYER 2 TURN »')
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('')
                print('✧ Player 2 has WON ✧')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('')
                    print('∵ TIE GAME! ∴')
                    game_on = False
                else:
                    turn = 'Player 1'
    
    if not replay():
        break
