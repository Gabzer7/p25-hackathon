#algoA*

def dist(P1, P2):
    
    i1, j1 = P1
    i2, j2 = P2
    distance_verticale = abs(i1 - i2)
    distance_horizontale = abs(j1 - j2)
    distance_totale = distance_verticale + distance_horizontale
    return distance_totale

#fonction qui prend pour arguments 
# les deux listes associées aux états solution  et grille (état courant) et qui renvoie 
# la fonction heuristique h(E,ER) égale à la somme des distances de chaque pièce dans
#  l'état grille à sa position dans l'état solution
def distance_h(grille, solution):
    total = 0  
    for i in range(3):  
        for j in range(3):  
            if grille[i][j] != '*':
                for x in range(3):
                    for y in range(3):
                        if solution[x][y] == grille[i][j]:
                            total += dist((i,j), (x,y))  
    return total