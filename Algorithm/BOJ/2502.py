D, K = list(map(int, input().split()))
# 1a + 0b, 0a + 1b, 1a + 1b, 1a + 2b, 2a + 3b, 3a + 5b, 5a + 8 b...
A = [0 for _ in range(30)]
B = [0 for _ in range(30)]

A[0] = 1
B[1] = 1

breaked = False

for i in range(2, D):
    A[i] = A[i-1] + A[i-2]
    B[i] = B[i-1] + B[i-2]

for i in range(1, K):
    for j in range(i, K):
        if A[D-1] * i + B[D-1] * j == K:
            print(i)
            print(j)
            breaked = True
            break
    
    if breaked == True:
        break