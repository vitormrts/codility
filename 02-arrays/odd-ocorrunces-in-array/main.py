# O(N**2)
# def solution(A):
#     if len(A) == 0:
#         return
#     B = []
#     for i in A:
#         if i not in B:
#             B.append(i)
#         else:
#             B.remove(i)
#     return B[0]


# O(N**2)
# def solution(A):
#      tam = len(A)
#      if tam == 0:
#          return
#      A.sort()
#      for i in range(tam):
#          if A.count(A[i]) > 1:
#              last_index = len(A) - 1 - A[::-1].index(A[0])
#              del A[:last_index + 1]
#          else:
#              return A[0]

# O(n log(n))
def solution(A):
    if len(A) == 0: # return none if len is 0
        return None
    elif len(A) == 1: # return the single element 
        return A[0]

    A.sort() # sort the array
    qntd = 0 
    # the logical of this algorithm is simple: we'll stores the amount that an element repeat in a variable and, everytime this item is different of sentinel,
    # we'll check the value of this amount. if that value is odd, we find the single element that is not even, then that is returned
    sentinela = A[0] 
    for item in A:
        if sentinela == item:
            qntd += 1
        else:
            if qntd % 2 == 0:
                qntd = 1
                sentinela = item
            else:
                return int(sentinela)
    if qntd % 2 != 0:
        return int(sentinela)


A = [5, 2, 2, 2, 2, 1, 1, 1, 1, 4, 4]
print(solution(A))