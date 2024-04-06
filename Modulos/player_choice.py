# Seção: Função para escolha da posição pelo jogador


def player_choice(board):
    while True:
        try:
            position = int(input('Choose a position: (1-9) '))
            if position in range(1, 10) and board[position] == ' ':
                return position
            else:
                print("Invalid position or position already taken. Please choose another position.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")