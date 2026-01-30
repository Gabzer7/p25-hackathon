import heapq

def etat_gagnant(n):
    # 1..n*n-1 puis 0
    return tuple(list(range(1, n*n)) + [0])

def est_gagnant(etat, n):
    return etat == etat_gagnant(n)

def voisins(etat, n):
    i0 = etat.index(0)
    r, c = divmod(i0, n)

    def echanger(i, j):
        lst = list(etat)
        lst[i], lst[j] = lst[j], lst[i]
        return tuple(lst)

    res = []
    if r > 0:      res.append(("U", echanger(i0, i0 - n)))
    if r < n - 1:  res.append(("D", echanger(i0, i0 + n)))
    if c > 0:      res.append(("L", echanger(i0, i0 - 1)))
    if c < n - 1:  res.append(("R", echanger(i0, i0 + 1)))
    return res

def resoudre_dijkstra(depart, n):
    if est_gagnant(depart, n):
        return []

    # dist[etat] = meilleur nombre de coups trouvé
    dist = {depart: 0}

    # Pour reconstruire la solution
    parent = {depart: None}         # parent[etat] = etat précédent
    coup_pour_aller = {depart: None} # coup_pour_aller[etat] = coup utilisé pour arriver ici

    # File de priorité : (distance, etat)
    pq = []
    heapq.heappush(pq, (0, depart))

    while pq:
        d, etat = heapq.heappop(pq)
        if d != dist[etat]:
            continue
        if est_gagnant(etat, n):
            coups = []
            cur = etat
            while parent[cur] is not None:
                coups.append(coup_pour_aller[cur])
                cur = parent[cur]
            coups.reverse()
            return coups
        for coup, nxt in voisins(etat, n):
            nd = d + 1
            if nxt not in dist or nd < dist[nxt]:
                dist[nxt] = nd
                parent[nxt] = etat
                coup_pour_aller[nxt] = coup
                heapq.heappush(pq, (nd, nxt))

    raise RuntimeError("Aucune solution trouvée (état peut-être impossible).")


# test
if __name__ == "__main__":
    n = 3
    depart = (1,2,3,4,5,6,7,0,8)  # 1 coup -> "R"
    sol = resoudre_dijkstra(depart, n)
    print(sol, len(sol))
