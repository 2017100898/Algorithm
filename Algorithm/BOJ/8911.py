N = int(input())

# 이 문제의 핵심 *_*
# x, y 둘 중 하나가 가장 작은 좌표 축 하나,
# 반대로 가장 큰 좌표축 하나를 찾으면 된다

for i in range(0, N):
    cmd = input().strip()

    # 현재의 x, y 그리고 거북이가 바라보는 방향(초기화 값은 N) 을 저장할 변수 만듦
    x, y, dir = 0, 0, "N"

    # min/max 값을 저장해둘 변수 만듦
    minx, miny = 0, 0
    maxx, maxy = 0, 0

    # L 명령어가 나오면 거북이가 바라보는 방향의 순서는 다음과 같음
    dir_L = ["N", "W", "S", "E"]
    # 반대로 R 명령어가 나오면 거북이가 바라보는 방향의 순서는 다음과 같음
    dir_R = ["N", "E", "S", "W"]

    for j in cmd:
        if j == "L":
            # L이 나오면 dir_L 의 순서대로 거북이의 고개를 돌려줌
            idx = dir_L.index(dir) + 1
            if idx == len(dir_L):
                dir = dir_L[0]
            else:
                dir = dir_L[idx]

        elif j == "R":
            # 반대로 R이 나올 때는 dir_R의 순서대로 거북이의 고개를 돌려줌
            idx = dir_R.index(dir) + 1
            if idx == len(dir_R):
                dir = dir_R[0]
            else:
                dir = dir_R[idx]

        elif j == "F":
            # F가 나오면 앞으로 가면 됨.
            # 이때, 바라보는 방향에 따라 x, y 의 값이 어떻게 변할지 결정 됨
            if dir == "N":
                y += 1
            elif dir == "E":
                x += 1
            elif dir == "W":
                x -= 1
            elif dir == "S":
                y -= 1

        elif j == "B":
            # B가 나올 때는 뒤로 가면 됨.
            # F와 마찬가지로 바라보는 방향에 따라 x, y 값이 결정 됨
            if dir == "N":
                y -= 1
            elif dir == "E":
                x -= 1
            elif dir == "W":
                x += 1
            elif dir == "S":
                y += 1

        # 매 업데이트 마다 minx, miny, maxx, maxy 값을 계산해서 업데이트 해줌
        minx, miny = min(x, minx), min(y, miny)
        maxx, maxy = max(x, maxx), max(y, maxy)

    # 최종적인 직사각형의 크기는 다음과 같음
    print(abs((maxx - minx) * (maxy - miny)))