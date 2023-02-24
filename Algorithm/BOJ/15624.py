P = int(input())
curr, next = 0, 1

for j in range(0, P+1):
    if j == 0 or j == 1:
        pass
    else:
        curr, next = next, (curr+next) % 1000000007

if P == 0 :
    print(curr)
else:
    print(next)
