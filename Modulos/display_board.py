# Seção: Funções de exibição do tabuleiro

def display_board(board):
    """
    Display the Tic Tac Toe board.
    """
    # Clear the screen
    print("\033[H\033[J")  # ANSI escape sequence to clear the screen
    
    print(board[7] + ' ┃ ' + board[8] + ' ┃ ' + board[9])
    print('─────────')
    print(board[4] + ' ┃ ' + board[5] + ' ┃ ' + board[6])
    print('─────────')
    print(board[1] + ' ┃ ' + board[2] + ' ┃ ' + board[3])
