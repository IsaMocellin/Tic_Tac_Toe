# Seção: Função para escolher o primeiro jogador


import random

def choose_first():
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'
