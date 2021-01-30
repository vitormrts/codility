# def solution(A):
#     if len(A) == 0:
#         return 1
#     elif len(A) == 1:
#         return A[0]
    
#     B = []
#     A.sort()
#     ultimo = False
#     #print(A)
#     if A[0] != 1:
#         B.append(1)

#     for i in range(1, len(A)):
#         if A[i] == len(A):
#             ultimo = True
            
#         if A[i] - A[i-1] > 1:
#             valor = A[i-1] + 1
#             B.append(valor)

#     print(valor)

    # if ultimo == False:
    #     B.append(len(A))
    #     print(len(A))
    
    # if len(B) > 1 and B[0] != B[1]:
    #     return  B[0], B[1]
    # elif len(B) == 1:
    #     print("A")
    #     return B[0]
    

# A = [2, 3, 1, 5]
# print(solution(A))
# solution(A)

def solution(A):
    n = len(A) + 1
    tot = n*(n+1)/2

    return int(tot - sum(A)) 
    
    #return B[0]



    # if A[0] != 1:
    #     B.append(1)

    # for i in range(1, len(A)):
    #     if A[i] - A[i-1] > 1:
    #         B.append(A[i])

A = [1, 2, 3, 5]
a = solution(A)
print(a)