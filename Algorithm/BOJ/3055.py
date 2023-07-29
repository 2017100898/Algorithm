from collections import deque
from copy import deepcopy

R, C = list(map(int, input().split()))
maps = []

for i in range(R):
    maps.append(list(input()))

waters = []
rocks = []
visit = []

# . : 비어있는 곳
# * : 물이 차있는 곳
# X : 돌
# D : 비버의 굴
# S : 고슴도치의 위치

# 고슴도치는 현재칸과 인접한 위치 (상하좌우)로 이동 가능
# 물이 차 있는 곳의 인접 위치는 물이 차게 된다
# 돌, 물 이동 불가 / 물은 비버의굴로 이동 불가

for i in range(R):
    for j in range(C):
        if maps[i][j] != '.':
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'D':
                D = (i, j)

            elif maps[i][j] == '*':
                waters.append((i, j))
            elif maps[i][j] == 'X':
                rocks.append((i, j))


def bfs(S, waters):
    result = 0
    # 고슴도치의 시작점을 기준으로 bfs 를 실행함
    que = deque([S])
    visit.append(S)
    tempQue = deque([])
    time = True

    # 고슴도치가 순회할 곳이 전혀 없을 때 아래 반복문을 끝낼 것임
    while True:
        # que 의 가장 첫 번째 요소 좌표를 뽑음        
        i, j = que.popleft()

        # time은 분(minute)을 뜻함
        # time이 True 가 되면, 1분이 지남을 의미하며 물이 확장되고, 고슴도치가 한번 이동함.
        # time이 False 일 때는 물이 확장되지 않고, 고슴도치가 이동할 수 있는 좌표들을 하나씩 고려하며, bfs 가 순회 되기만 함.
        if time == True:
            copyWaters = deepcopy(waters)
            # 물의 영역 확장
            for k, n in copyWaters:
                if k - 1 >= 0 and (k-1, n) not in waters and (k-1, n) != D and (k-1, n) not in rocks and (k-1, n) not in copyWaters:
                    waters.append((k-1, n))
                if n - 1 >= 0 and (k, n-1) not in waters and (k, n-1) != D and (k, n-1) not in rocks and (k, n-1) not in copyWaters:
                    waters.append((k, n-1))
                if k + 1 < R and (k+1, n) not in waters and (k+1, n) != D and (k+1, n) not in rocks and  (k+1, n) not in copyWaters:
                    waters.append((k+1, n))
                if n + 1 < C and (k, n+1) not in waters and (k, n+1) != D  and (k, n+1) not in rocks and  (k, n+1) not in copyWaters:
                    waters.append((k, n+1))
            time = False

        # 고슴도치의 이동가능한 영역을 bfs queue 에 담아줌
        if i - 1 >= 0 and (i-1, j) not in waters and (i-1, j) not in rocks and (i-1, j) not in tempQue:
            # 비버의 굴에 도착하면 결과를 반환
            if (i-1, j) == D:
                result += 1
                return result
            # 도착이 아니라면, 방문했음을 표시하고, 다음 시간에 고려될 queue 이기에 tempQue 라는 queue 대기열에 좌표들을 넣음
            else:
                visit.append((i-1, j))
                tempQue.append((i-1, j))
                
        if j - 1 >= 0 and (i, j-1) not in waters and  (i, j-1) not in rocks and  (i, j-1) not in tempQue:
            if (i, j-1) == D:
                result += 1
                return result
            else:
                visit.append((i, j-1))
                tempQue.append((i, j-1))

        if i + 1 < R and (i+1, j) not in waters and (i+1, j) not in rocks and (i+1, j) not in tempQue :
            if (i+1, j) == D:
                result += 1
                return result
            else:
                visit.append((i+1, j))
                tempQue.append((i+1, j))
        
        if j + 1 < C and  (i, j+1) not in waters and (i, j+1) not in rocks  and (i, j+1) not in tempQue:
            if (i, j+1) == D:
                result += 1
                return result
            else:
                visit.append((i, j+1))
                tempQue.append((i, j+1))

        # 1분뒤에 고려될 queue 가 비어있고, 대기열 (tempQue)도 비어있으면 반복문을 끝냄
        if len(que) == 0:
            if len(tempQue) == 0:
                return 0
            # 1분뒤에 고려될 queue 가 비어있고, 대기열이 비어있지않으면, 대기열의 좌표들을 queue에 넣어 다음 1분동안 고려될 수 있도록 만들어줌
            else:
                que = deepcopy(tempQue)
                tempQue = deque([])
                result += 1
                time = True

results = bfs(S, waters)
if results == 0:
    print("KAKTUS")
else:
    print(results)