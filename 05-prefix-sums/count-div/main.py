def solution(A, B, K):
    if A % K == 0:
        z = 1
    else:
        z = 0

    x = A//K
    y = B//K

    return y - x + z
    

a = solution(0, 0, 5)
print(a)