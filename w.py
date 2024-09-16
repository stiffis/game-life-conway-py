from colorama import Back, Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# Matriz 3x3 de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para imprimir la matriz con resaltado de fondo
def print_matrix(matrix):
    for fila in matrix:
        for row in fila:
            # Resaltar las celdas con fondo verde y texto blanco
            print(Back.GREEN + Fore.BLACK + f"  ", end="")  # Espacio adicional para separación
        print()# Nueva línea al final de cada fila

# Llamar a la función para imprimir la matriz
#print_matrix(matriz)
x=int(input("Ingrese la cantidad de filas: "))
y=int(input("Ingrese la cantidad de columnas: "))
matrix = []
for i in range(x):
    
    for j in range(y):
        print(Back.BLUE + f"  ", end="|")
    print()




