cmd = list(map(int, input().split()))
N, M = cmd[0], cmd[1]

sets = list()

for i in range(0, N):
    sets.append(int(input()))

# 동전 리스트를 큰 순서대로 정렬
sets.sort(reverse=True)

# 사용한 동전의 개수를 저장할 변수
S = 0

# 동전 리스트를 순회하며, 타겟 금액에서 큰 동전부터 빼는 작업을 실시
# 타겟 금액에서 동전을 뺐을 때 0보다 작은 숫자가 되면, 패스
# 0보다 큰 숫자가 남으면, 0보다 작아질 때까지 같은 동전을 사용 및 총 개수 + 1
for j in sets:
    if M - j < 0 :
        pass
    else:
        while M - j >= 0 :
            M -= j
            S+=1

print(S)
