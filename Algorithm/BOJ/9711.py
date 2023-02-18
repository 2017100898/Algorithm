import sys
T = int(input())

for i in range(0, T):
    result = list()

    PQ = sys.stdin.readline().split()
    P, Q = int(PQ[0]), int(PQ[1])

    curr, next = 1, 1

    for j in range(0, P):
        if j == 0 or j == 1:
            pass
        else:
            curr, next = next, curr+next
        
    
    print(f"Case #{i+1}: {next % Q}")