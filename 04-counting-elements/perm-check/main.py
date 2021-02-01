def solution(A):
    A.sort()
    count = 0
    for i in range(len(A)):
        if A[i] == i+1:
            count += 1
        else:
            break
    
    if count == len(A):
        return 1
    return 0

    # aux = [0]*(len(A))
    
    # for i, elem in enumerate(A):


A = [4, 1, 3]
a = solution(A)
print(a)