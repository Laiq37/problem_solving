def queensAttack(n, k, r_q, c_q, obstacles):
    lDiagTop = min(n-r_q, c_q-1)
    rDiagTop = min(n-r_q, n-c_q)
    lDiagBot = min(r_q-1,c_q-1)
    rDiagBot = min(r_q-1, n-c_q)
    totalMoves = lDiagTop+rDiagTop+lDiagBot+rDiagBot+((n-1)*2)
    for i in range(0,len(obstacles)):
        if abs(obstacles[i][0]-r_q) == abs(obstacles[i][1]-c_q):
            if obstacles[i][1] < c_q:
                totalMoves -= (obstacles[i][1],n-obstacles[i][0]+1)
            elif obstacles[i][1]>c_q:
                # totalMoves -= c_q-obstacles[i][1]-c_q+1
                totalMoves -= min(n-obstacles[i][1]+1,obstacles[i][0])
        if obstacles[i][0] == r_q:
            if obstacles[i][1] > c_q:
                totalMoves -=n-obstacles[i][1]+1
            else:
                totalMoves -=obstacles[i][1]
        elif obstacles[i][1] == c_q:
            if obstacles[i][0] > r_q:
                totalMoves -=n-obstacles[i][1]+1
            else:
                totalMoves -=obstacles[i][0]
    return totalMoves
queensAttack(5,3,4,3,[[5, 5], [4, 2], [2, 3]])