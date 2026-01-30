import pygame
import sys
import random

pygame.init()

#  On configure l'esthétique
TAILLE = 300
CASE = 100
HAUTEUR_TOTAL = 400 

#  couleurs
BLEU_NUIT = (30, 30, 50)       # Fond
TURQUOISE = (20, 160, 180)     # Tuiles
ORANGE = (255, 140, 0)         # Survol souris
VERT_VICTOIRE = (46, 204, 113) # Victoire
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

screen = pygame.display.set_mode((TAILLE, HAUTEUR_TOTAL))
pygame.display.set_caption("Jeu du taquin")

font = pygame.font.SysFont("arial", 50, bold=True)
small_font = pygame.font.SysFont("arial", 24)

# code du jeu
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

# code pour l'esthétique du jeu 
def dessine():
    
    screen.fill(BLEU_NUIT)
    
    # Position de la souris 
    mx, my = pygame.mouse.get_pos()

    # Dessin des cases
    for i in range(3):
        for j in range(3):
            val = grille[i][j]
            
            if val != '*':
              
                rect = pygame.Rect(j*CASE + 5, i*CASE + 5, CASE - 10, CASE - 10)
                
              
                couleur_tuile = TURQUOISE
                if rect.collidepoint((mx, my)) and not gagne:
                    couleur_tuile = ORANGE
                
                # on rend les rectangles arrondis
                pygame.draw.rect(screen, couleur_tuile, rect, border_radius=10)
                pygame.draw.rect(screen, BLANC, rect, 2, border_radius=10) 

               
                txt = font.render(str(val), True, BLANC)
                rect_txt = txt.get_rect(center=rect.center)
                screen.blit(txt, rect_txt)

    # Zone du bas 
    # Le fond change en vert si on gagne
    couleur_fond_bas = VERT_VICTOIRE if gagne else BLEU_NUIT
    pygame.draw.rect(screen, couleur_fond_bas, (0, 300, 300, 100))
    pygame.draw.line(screen, BLANC, (0, 300), (300, 300), 3)

    # Affichage du score
    info = small_font.render(f"Coups : {nbcoups}", True, BLANC)
    screen.blit(info, (20, 340))

    if gagne:
        msg = small_font.render("Gagné !", True, BLANC)
        screen.blit(msg, (150, 340))
 


clock = pygame.time.Clock()

# boucle principale
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
