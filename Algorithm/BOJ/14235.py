# 거점을 방문한 횟수 n을 입력 받음
n = int(input())

# 선물의 가치를 입력할 리스트
pq = list()

# 결과를 저장할 리스트
result = list()

for i in range(0, n):
    a = input()
    lst = a.split()
    # List element 형변환
    lst = [int(s) for s in lst]

    if int(lst[0]) == 0:
        # pq에 값이 없을 경우, result에 -1 append
        if len(pq) == 0:
            result.append(-1)

        else:
            # 가장 큰 값 pop, result에 append
            result.append(max(pq))
            pq.remove(max(pq))
            
    else:
        # 0이 아닌 수를 입력 받았을 때는
        # 가장 먼저 입력한 수에 맞게 순회하며
        # 선물의 가치를 pq에 입력
        for j in range(1, int(lst[0])+1):
            pq.append(lst[j])
        
            
# 결과 리스트 순회하며 값 출력
for i in result:
    print(i)
            