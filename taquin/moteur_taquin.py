def etat_gagnant(n):
    # 1..n*n-1 puis 0
    return tuple(list(range(1, n*n)) + [0])

def est_gagnant(etat, n):
    return etat == etat_gagnant(n)

# Test rapide
n = 3
print(etat_gagnant(n))
print(est_gagnant(etat_gagnant(n), n))  # True
