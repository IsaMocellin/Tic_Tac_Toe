# Seção: Função para entrada de jogadores

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while marker.upper() != 'X' and marker.upper() != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'
            
    return (player1, player2)
