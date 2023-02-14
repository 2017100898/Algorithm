import heapq

N = int(input())
time = list()
Room = list()

# 모든 강의 시간을 입력 받아서 time List 에 넣고 정렬
for i in range(0, N):
    time.append(list(map(int, input().split())))

time.sort()

# 강의실 개수를 구할 PQ 생성 및 가장 먼저 시작하는 강의실의 종료시간을 입력
heapq.heappush(Room, time[0][1])

# 2번째 수업부터 순회
for i in range(1, N):
    # PQ에 입력되어있는 수업의 종료시간보다 먼저 시작하는 수업이라면,
    # 강의실을 하나 더 생성해야하므로 새롭게 Room PQ에 종료 시간을 추가
    if time[i][0] < Room[0]:
        heapq.heappush(Room, time[i][1])
    else:
    # PQ에 입력되어있는 수업의 종료시간보다 늦게 시작하는 수업이라면
    # 기존의 수업을 없애고, 새로운 수업의 종료 시간을 넣어줌
        heapq.heappop(Room)
        heapq.heappush(Room, time[i][1])

# 필요한 강의실 개수를 Return
print(len(Room))