from graphviz import Digraph, Source
from IPython.display import display

from pylab import*

ER=[[1,2,3],[4,5,6],[7,8,'*']] #état de référence=état final à atteindre
E=[[5, 2, 3], [1, 4, '*'], [7, 8, 6]]  #état de départ à faire varier parmi les états accessibles depuis l'état final

#Affichage provisoire d'un état
def affiche(E):
    L=len(E)
    C=len(E[0])
    xlim(-1,C+1)
    ylim(-1,L+1)
    plot([0,C,C,0,0],[0,0,L,L,0],'b-',lw=3) #COMMENTER
    for i in range(1,L):
        plot([0,C],[i,i],'k-',lw=2) #COMMENTER
    for j in range(1,C):
        plot([j,j],[0,L],'k-',lw=2) #COMMENTER
    for i in range(0,L):
        for j in range(0,C):
            text(j+0.4,L-i+0.3-1,E[i][j],fontsize=24) #COMMENTER

#Test d'affichage
close()
affiche(E)
show()