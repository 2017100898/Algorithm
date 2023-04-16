from itertools import combinations

cmd = input().split()
N, M = int(cmd[0]), int(cmd[1])
Map = list()
house = list()
chicken = list()

# 각 칸은 빈칸, 치킨집, 집 중 하나이다
# Map 을 입력 받는다
for i in range(0, N):
    Map.append(list(map(int, input().split())))

# Map의 정보를 통해 집과 치킨 집 좌표 정보를 나누어 정리한다
for i in range(0, N):
    for j in range(0, N):
        if Map[i][j] == 1:
            house.append((i + 1, j + 1))
        elif Map[i][j] == 2:
            chicken.append((i + 1, j + 1))

result_dist = 9999999

# 치킨 집 중 M개만 선택하는 것은 조합을 통해 해결할 수 있다
for x in combinations(chicken, M):
    city_dist = 0
    # 최단 거리 계산을 위해 집 중 하나를 선택한다
    for h in house:
        chicken_dist = 9999999
        # 조합에서 선택된 M개의 치킨집 중 하나를 선택한다
        for k in x:
            # 치킨집과 집의 거리를 구하고 최단 거리를 업데이트 하는 과정을 For문을 통해 반복한다
            chicken_dist = min(chicken_dist, abs(h[0]-k[0]) + abs(h[1]-k[1]))
        city_dist += chicken_dist
    # 모든 조합에 대해 최단 거리를 업데이트 해준다
    result_dist = min(result_dist, city_dist)

print(result_dist)