import pygame
import sys


# DEFINIMOS EL NUMERO DE REINAS
N = 30
QUEEN_IMAGE = pygame.image.load('reina2.png')

# DEFINIMOS EL TAMA;O DEL TABLERO DE AJEDREZ
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // N

# COLORES
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

# VERIFICA SI ES SEGURO COLOCAR UNA REINA EN LA POSICION (FILA, COLUM)
def is_secure(tablero, fila, columna):
    
    # VERIFICA LA COLUMNA
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # VERIFICA LA DIAGONAL SUPERIOR IZQUIERDA
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # VERIFICA LA DIAGONAL SUPERIOR DERECHA
    for i, j in zip(range(fila, -1, -1), range(columna, N)):
        if tablero[i][j] == 1:
            return False
    
    return True

def solve_queens(tablero, fila):
    if fila == N:
        return True
        
    for columna in range(N):
        if is_secure(tablero, fila, columna):
            tablero[fila][columna] = 1
            if solve_queens(tablero, fila + 1):
                return True
            tablero[fila][columna] = 0
    
    return False

def draw_tablero(tablero):
    for fila in range(N):
        for columna in range(N):
            color = WHITE if (fila + columna) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (columna * SQUARE_SIZE, fila * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for fila in range(N):
        for columna in range(N):
            if tablero[fila][columna] == 1:
                queen_rect = QUEEN_IMAGE.get_rect()
                queen_rect.center = (columna * SQUARE_SIZE + SQUARE_SIZE // 2, fila * SQUARE_SIZE + SQUARE_SIZE // 2)
                screen.blit(QUEEN_IMAGE,queen_rect.topleft )
                #pygame.draw.circle(screen, RED, (columna * SQUARE_SIZE + SQUARE_SIZE // 2, fila * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('N reinas')

tablero = [[0 for _ in range(N)] for _ in range(N)]

if solve_queens(tablero, 0):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        draw_tablero(tablero)
        pygame.display.flip()

pygame.quit()
sys.exit()