def solution(A, K):
    length = len(A)
    
    if length == 0 or K % length == 0 or length == A.count(0):
        return(A)
    else:
        B = []
        if K > length:
            K %= length
        for i in range(K):
            B.append(A.pop())
        B.reverse()
        return(B+A)
    pass


A = [3, 8, 9, 7, 6]
print(solution(A, 23))
