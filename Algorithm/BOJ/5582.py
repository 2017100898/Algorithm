# [5582] 공통 부분 문자열
# 다이나믹 프로그래밍
# 문자열

word1 = str(input())
word2 = str(input())
matrix = [[0 for x in range(len(word1))] for y in range(len(word2))] 
result = 0

for i in range(0, len(word1)):
    for j in range(0, len(word2)):
        if word1[i] == word2[j]:
            if (j!=0 and i!=0 and matrix[j-1][i-1] > 0):
                matrix[j][i] = matrix[j-1][i-1]+1
            else:
                matrix[j][i] = 1
            
            if result < matrix[j][i]:
                result = matrix[j][i]
            
        else:
            matrix[j][i] = 0
            
    
print(result)