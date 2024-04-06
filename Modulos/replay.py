# Seção: Função para perguntar ao jogador se deseja jogar novamente

def replay():
    print('')
    choice = input('Play again? Enter (Yes/No) ')
    print('')
    return choice.lower() == 'yes'
