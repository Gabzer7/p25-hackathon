import pygame
import sys
import random

pygame.init()

# ======================
# PARAMÈTRES
# ======================
TAILLE = 300
CASE = 100
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Jeu du taquin")

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 24)

def voisins(pos):
    i, j = pos
    v = []
    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            v.append((ni, nj))
    return v

def position_val(E, val):
    for i in range(3):
        for j in range(3):
            if E[i][j] == val:
                return i, j
def intervertit(E, pos):
    i0, j0 = position_val(E, '*')
    i, j = pos
    E[i0][j0], E[i][j] = E[i][j], E[i0][j0]
            
def melange(E, n=100):
    for _ in range(n):
        pos_vide = position_val(E, '*')
        voisins_pos = voisins(pos_vide)
        intervertit(E, random.choice(voisins_pos))

ER = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, '*']]

E = [ligne[:] for ligne in ER]
melange(E)

nbcoups = 0
gagne = False







def intervertit(E, pos):
    i0, j0 = position_val(E, '*')
    i, j = pos
    E[i0][j0], E[i][j] = E[i][j], E[i0][j0]


# ======================
# AFFICHAGE
# ======================
def dessine():
    screen.fill(BLANC)

    for i in range(4):
        pygame.draw.line(screen, NOIR, (0, i*CASE), (300, i*CASE), 2)
        pygame.draw.line(screen, NOIR, (i*CASE, 0), (i*CASE, 300), 2)

    for i in range(3):
        for j in range(3):
            if E[i][j] != '*':
                txt = font.render(str(E[i][j]), True, NOIR)
                rect = txt.get_rect(center=(j*CASE+50, i*CASE+50))
                screen.blit(txt, rect)

    info = small_font.render(f"Coups : {nbcoups}", True, NOIR)
    screen.blit(info, (10, 330))

    if gagne:
        msg = small_font.render("Gagné 🎉", True, NOIR)
        screen.blit(msg, (200, 330))


# ======================
# BOUCLE JEU
# ======================
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gagne:
            x, y = event.pos
            if y < 300:
                i, j = y // CASE, x // CASE
                if (i, j) in voisins(position_val(E, '*')):
                    intervertit(E, (i, j))
                    nbcoups += 1
                    if E == ER:
                        gagne = True

    dessine()
    pygame.display.flip()
    clock.tick(30)
