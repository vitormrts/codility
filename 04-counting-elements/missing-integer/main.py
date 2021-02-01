def solution(A):
    A.sort()
    print(A)
    smallest = 1
    for number in A:
        if number == smallest:
            smallest = smallest + 1
        if number > smallest:
            break
    return smallest


A = [1, 3, 6, 4, 1, 2]
a = solution(A)
print(a)