N = int(input())
A = []

elem = 0

for i in range(N):
    a = int(input())
    A.append((a, elem))
    elem += 1

sortedA = sorted(A)

maxElem = 0

for i in range(N):
    if maxElem < sortedA[i][1] - i:
        maxElem = sortedA[i][1] - i

print(maxElem + 1)
