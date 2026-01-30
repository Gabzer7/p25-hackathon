import pygame
import sys
import random

pygame.init()

#on fixe les paramètres de l'interface
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

def trouve_case(grille, val):  
    for i in range(3):
        for j in range(3):
            if grille[i][j] == val:
                return i, j
            
def intervertit(grille, pos):
    i0, j0 = trouve_case(grille, '*')
    i, j = pos
    grille[i0][j0], grille[i][j] = grille[i][j], grille[i0][j0]



solution = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, '*']]

def melange(grille, n=50):  
    for _ in range(n):
        vide = trouve_case(grille, '*')  
        voisins_pos = voisins(vide)
        i,j = random.choice(voisins_pos)  
        intervertit(grille, (i,j)) 

grille = [ligne[:] for ligne in solution]
melange(grille)

            




nbcoups = 0
gagne = False






def dessine():
    screen.fill(BLANC)

    pygame.draw.line(screen, NOIR, (0, 0), (300, 0), 2)  
    pygame.draw.line(screen, NOIR, (0, 100), (300, 100), 2) 
    pygame.draw.line(screen, NOIR, (0, 200), (300, 200), 2)  
    pygame.draw.line(screen, NOIR, (0, 300), (300, 300), 2)  
    pygame.draw.line(screen, NOIR, (0, 0), (0, 300), 2)  
    pygame.draw.line(screen, NOIR, (100, 0), (100, 300), 2)  
    pygame.draw.line(screen, NOIR, (200, 0), (200, 300), 2)  
    pygame.draw.line(screen, NOIR, (300, 0), (300, 300), 2) 

    for i in range(3):
        for j in range(3):
            if grille[i][j] != '*':
                txt = font.render(str(grille[i][j]), True, NOIR)
                rect = txt.get_rect(center=(j*CASE+50, i*CASE+50))
                screen.blit(txt, rect)

    info = small_font.render(f"Coups : {nbcoups}", True, NOIR)
    screen.blit(info, (10, 330))

    if gagne:
        msg = small_font.render("Gagné 🎉", True, NOIR)
        screen.blit(msg, (200, 330))



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
                vi, vj = trouve_case(grille, '*')
                if (i,j) in [(vi-1,vj),(vi+1,vj),(vi,vj-1),(vi,vj+1)]: 
                    intervertit(grille, (i, j))
                    nbcoups += 1
                    if grille == solution:
                        gagne = True

    dessine()
    pygame.display.flip()
    clock.tick(30)
