## 18438 LCS 2

s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

mat = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
ans = ""

for j in range(1, l1 + 1):
    for i in range(1, l2 + 1):
        if s1[j - 1] == s2[i - 1]:
            mat[i][j] = mat[i - 1][j - 1] + 1

        else:
            mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

print(mat[-1][-1])

while i > 0 and j > 0:
    if s1[j - 1] == s2[i - 1]:
        ans += s1[j - 1]
        i -= 1
        j -= 1

    elif mat[i - 1][j] > mat[i][j - 1]:
        i -= 1
    
    else:
        j -= 1

if len(ans) > 0:
    print(ans[::-1])

