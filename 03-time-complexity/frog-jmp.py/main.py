def solution(X, Y, D):
    if X == Y:
        return 0
    distancia = Y - X
    passos = distancia / D
    if passos.is_integer() is False:
        passos += 1
    return int(passos)
    
print(solution(1, 6, 4))