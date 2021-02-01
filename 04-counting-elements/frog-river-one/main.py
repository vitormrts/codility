def solution(X, A):
    folhas = [0]*X
    i = 0
    soma = X
    
    for folha in A:
        if folha <= X and folhas[folha-1] == 0:
            soma -= 1
            folhas[folha-1] = 1
        if soma == 0:
            return i
        i += 1
    return -1


A = [1, 3, 1, 4, 2, 3, 5, 4]
a = solution(5, A)
print(a)