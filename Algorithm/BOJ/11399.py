N = int(input())
M = list(map(int, input().split()))
# 인출 시간이 작은 순으로 정렬
M.sort()

# 가장 첫 사람의 인출 시간을 S로 설정
S = M[0]

# 리스트를 순회하며, 
# M[i] 를 M[i-1] 까지의 인출 시간 + M[i]의 인출 시간으로 업데이트
for i in range(1, len(M)):
    M[i] += S
    S = M[i]

# M을 모두 더하여, 총 인출 시간을 구함
print(sum(M))