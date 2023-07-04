# N x M 크기의 보드를 찾았다
# 어떤 정사각형은 검은색, 어떤 것은 흰색
# 이것을 잘라서 8 x 8 크기의 체스판으로 만들려고 한다
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 하고, 
# 변을 공유하는 두개의 사각형은 다른 색이어야 한다
# 8 x 8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠하는 것이 목표
# 다시 칠해야하는 정사각형의 최소 개수?


N, M = list(map(int, input().split()))
matrix = list()
result = list()

for n in range(N):
    m = list(input())
    matrix.append(m)

# matrix를 순회
for n in range(N - 7):
    for m in range(M - 7):
        # 첫 단어를 W로 만들 때 수정해야되는 경우의 수를 기록할 변수
        white = 0
        # 첫 단어를 B로 만들 때 
        black = 0

        # 첫 단어를 W로 만들 때, a + b 이 2의 배수인 cell에 대해서는 B여야 한다
        # 반대로 B로 만들 때, a + b 이 2의 배수인 cell에 대해서는 W여야 한다
        # 첫 단어를 W로 만들 때, a + b 이 2의 배수가 아닌 cell에 대해서는 W여야 한다
        # 반대로 B로 만들 때, a + b 이 2의 배수가 아닌 cell에 대해서는 B여야 한다
        for a in range(n, n + 8):
            for b in range(m, m + 8):
                if (a + b) % 2 == 0:
                    if matrix[a][b] == 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if matrix[a][b] == 'B':
                        white += 1
                    else:
                        black += 1

        result.append(white)
        result.append(black)
        
print(min(result))