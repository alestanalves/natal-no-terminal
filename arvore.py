import os
import time
import random
from colorama import Fore, Style, init
#lembrese se rodar o comando pip install colorama

# Inicializa o colorama para garantir que funcione no Windows
init()

def clear_terminal():
    """Função para limpar o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_christmas_tree(height):
    """Cria uma árvore de Natal com enfeites que piscam."""
    tree = []
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        leaves = ''.join(random.choice(['*', 'o', '^']) if j % 2 == 0 else '^' for j in range(2 * i + 1))
        tree.append(spaces + leaves)

    # Adiciona o tronco
    trunk = (' ' * (height - 2) + '||')
    tree.extend([trunk] * 2)  # Tronco com duas linhas

    return tree

def display_message():
    """Exibe uma mensagem abaixo da árvore."""
    message = """
    Feliz Natal 2024! 
    """
    print(Fore.CYAN + message + Style.RESET_ALL)

def display_tree(tree):
    """Exibe a árvore no terminal com efeitos."""
    colors = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE]
    while True:
        clear_terminal()
        for line in tree:
            # Colore os enfeites e folhas
            colored_line = ''.join(
                random.choice(colors) + char + Style.RESET_ALL if char in ['*', 'o', '^'] else Fore.GREEN + char + Style.RESET_ALL
                for char in line
            )
            print(colored_line)
        display_message()
        time.sleep(0.5)

if __name__ == "__main__":
    height = 15
    tree = create_christmas_tree(height)
    display_tree(tree)
