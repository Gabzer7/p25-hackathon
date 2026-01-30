# On commence par créer le graphe de toutes les configurations possibles 

from collections import deque

class Board:

    def __init__(self, l):
      self.positions = tuple(l)

    def __eq__(self, other):
      return self.positions == other.positions
   
    def __hash__(self):
      return hash(self.positions)

def voisins(configuration):  # renvoie les 4 configurations suivantes possibles en fonction de celle donnée au départ
    voisins = []
    i = configuration.index(0) # recherche le 0 dans le jeu
    (ligne,col) = (i//3, i%3)

    deplacements = [(-1,0), (1,0), (0,-1), (0,1)]

    for dl, dc in deplacements:
        nl, nc = ligne + dl, col + dc
        if 0<=nl< 3 and 0<=nc<3:
            j = nl*3 + nc # index de la nouvelle position du 0
            nouvelle_config = configuration.copy()
            nouvelle_config[i], nouvelle_config[j] = nouvelle_config[j], nouvelle_config[i]
            voisins.append(nouvelle_config)

    return voisins

def construire_graphe(config_initiale):
    graphe = {}
    vues = set ()
    file = deque([config_initiale])

    while file:
        config = file.popleft()
        if config in vues:
            continue 
        vues.add(config)
        graphe[config] = voisins(config)

        for v in graphe[config]:
            if v not in vues:
                file.append(v)
    
    return graphe 

