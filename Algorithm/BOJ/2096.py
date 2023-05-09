# 아랫줄로 내려갈 때는 바로 아래의 수로 내려가거나, 아래 수와 붙어있는 수로만 이동할 수 있음
N = int(input())

dp_min = []
dp_max = []

for i in range(0, N):
    # N 수만큼 순회하며 num 입력 받음
    num = list(map(int, input().split()))
    
    # 첫 행에 대해서는 dp_min과 dp_max에 세 개의 값을 각각 저장을 해준다
    if i == 0:
        dp_min.append(num)
        dp_max.append(num)

    # 두 번째 행부터는 dp_min과 dp_max를 계산할 거임
    else:
        dp_min.append([0] * 3)
        dp_max.append([0] * 3)

        for j in range(0, 3):
            # 첫 열일 경우, 이전 행에서 첫번째와 두번째 열의 값 중 (작은/큰) 값을 가져와서 현재의 값과 더해준다
            if j == 0:
                dp_min[1][0] = num[0] + min(dp_min[0][0], dp_min[0][1])
                dp_max[1][0] = num[0] + max(dp_max[0][0], dp_max[0][1])
            #  두번째 열일 경우, 이전 행에서 모든 열의 값 중 (작은/큰) 값을 가져와서 현재의 값과 더해준다
            elif j == 1:
                dp_min[1][1] = num[1] + min(dp_min[0][0], dp_min[0][1], dp_min[0][2])
                dp_max[1][1] = num[1] + max(dp_max[0][0], dp_max[0][1], dp_max[0][2])
            # 마지막 열일 경우, 이전 행에서 두번째와 마지막 열의 값 중 (작은/큰) 값을 가져와서 현재의 값과 더해준다
            elif j == 2:
                dp_min[1][2] = num[2] + min(dp_min[0][2], dp_min[0][1])
                dp_max[1][2] = num[2] + max(dp_max[0][2], dp_max[0][1])

        #메모리 절약을 위해 dp의 첫 행을 매번 지워준다.
        dp_min.pop(0)
        dp_max.pop(0)

print(max(dp_max[-1]), min(dp_min[-1]), sep=' ')
