import sys
import heapq

init = input().split() # N, M, K를 입력 받음

N = int(init[0]) #축제가 열리는 기간 (기간 만큼 술 먹을 수 있음)
M = int(init[1]) #채워야하는 선호도 합
K = int(init[2]) #마실수 있는 맥주 종류의 수

# 입력받은 각 맥주의 선호도와 도수를 저장하기 위한 리스트
lst = list()

# 마실 맥주를 선택하기 위한 Priority Queue
pq = list()

like = 0
min = 0
find = False

# 맥주의 c가 간 레벨보다 높으면 기절
# N 개의 선호도 합이 M 이상이고 싶음 (불가능시 -1 출력)

# lst에 각 맥주의 선호도와 도수를 입력받아 저장
for i in range(0, K):
    vc = sys.stdin.readline().split()
    v, c = int(vc[0]), int(vc[1])
    lst.append((v, c))

# 도수로의 오름차순 정렬
lst.sort(key=lambda x:(x[1], x[0]))

# lst를 순회하며 도수가 낮은 술의 선호도부터 하나씩 pq에 넣음
# pq는 선호도 순으로 내림차순 정렬
for i in range(0, K):
    heapq.heappush(pq, lst[i][0])
    
    like += lst[i][0]
    min = lst[i][1]
    
    # pq의 리스트가 N과 같아질 때 선호도가 M을 넘었는지 판단 후 맞을 경우 break
    if(len(pq) == N):
        if(like >= M):
            find=True
            print(min)
            break
        # 선호도가 M을 넘지 않았을 경우 선호도가 가장 작은 술 삭제
        else:
            like-=heapq.heappop(pq)

# 조건 충족 불가시 -1 반환
if not find:
    print(-1)