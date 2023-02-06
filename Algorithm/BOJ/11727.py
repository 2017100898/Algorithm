# n 입력 받음
n = int(input())

# 1 x 2 | 2 x 1 | 2 x 2 타일로 2 x n 타일을 채워야 함
# n = 1 : 1
# n = 2 : 3
# n = 3 : 5
# n = 4 : 11 => result[n] = result[n-1] * 2 + result[n-2] 라는 것을 알 수 있음

# n=2, 3 일 때의 값을 각각 curr, next에 넣어두고
# 4 이상의 값이 나왔을 때부터 For문으로 점화식 계산

curr = 3
next = 5

if n == 1 :
    print(1)
elif n == 2:
    print(3)
elif n == 3:
    print(5)
else:
    for i in range(3, n):
        curr, next = next, curr * 2 + next

    print(next % 10007)