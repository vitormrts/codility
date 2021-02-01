def solution(A):
    aux = len(A)-1
    first_part = []
    second_part = []
    
    for i in range(len(A)-1):
        if i == 0 and aux == len(A) - 1:
            first_part.append(A[i])
            second_part.append(A[aux])
        else:
            first_part.append(first_part[i-1] + A[i])
            second_part.append(second_part[i-1] + A[aux])
        aux -= 1

    aux = len(A) - 1
    min_value = 0

    for i in range(len(first_part)):
        gap = first_part[i] - second_part.pop()
        if gap < 0:
            gap *= -1
        if gap < min_value or i == 0:
            min_value = gap
        aux -= 1
    
    print(min_value)


A = [3, 5, 7, 9, 13, 4]
solution(A)



