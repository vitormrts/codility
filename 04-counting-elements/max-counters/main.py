# def solution(N, A):
#     contadores = [0]*N
#     max_value = 0

#     for k in range(len(A)):
#         if 1 <= A[k] <= N:
#             contadores[A[k]-1] += 1
#             if contadores[A[k]-1] > max_value:
#                 max_value = contadores[A[k]-1]
#         else:
#             contadores = [max_value]*N
#     return contadores

def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for K,X in enumerate(A): 
        if 1 <= X <= N:
            counters[X-1] = max(counters[X-1], last_update)
            counters[X-1] += 1
            max_counter = max(counters[X-1], max_counter)
        elif A[K] == (N + 1):
            last_update = max_counter

    for i in range(N): 
        counters[i] = max(counters[i], last_update)

    return counters



A = [3, 4, 4, 6, 1, 4, 4]
print(solution(5, A))