
from colorama import Fore, Back, Style, init

# Inicializa colorama
init(autoreset=True)

# Definir bordes de la matriz
def print_matrix():
    print(Fore.BLUE + '+---+---+---+')  # Borde superior
    for _ in range(3):
        print(Fore.BLUE + '|', end='')   # Borde izquierdo
        print('   |   |   |')           # Espacios vacíos
        print(Fore.BLUE + '+---+---+---+')  # Borde inferior/interior

# Llamar a la función para imprimir la matriz
print_matrix()
