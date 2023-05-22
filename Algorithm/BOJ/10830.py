NB = input().split()
N, B = int(NB[0]), int(NB[1])
A = []

for i in range(0, N):
    A.append(list(map(int, input().split())))

def mul(A, B):
    N = len(A)
    c = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            e = 0
            for k in range(N):
                e += A[i][k] * B[k][j]
            c[i][j] = e % 1000
    return c

def power(A, N):
    if N == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    
    a = power(A, N // 2)
    if N % 2 == 0:
        return mul(a , a)
    
    else:
        return mul(mul(a, a), A)
    
result = power(A, B)
for i in result:
    print(*i, sep=" ")