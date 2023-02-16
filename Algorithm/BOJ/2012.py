import sys 

# 입력할 숫자의 개수 N을 입력
N = int(input())

# 입력한 숫자들을 담을 list
lst = [0] * N

result = 0

# N개의 예상 등수를 입력 받음
for i in range(0, N):
    lst[i] = int(sys.stdin.readline())

# lst 정렬 : 이 부분 2중 For문으로 짰다가 시간초과 남 ㅠ,ㅠ
lst.sort()

# 정렬한 list를 1등부터 N등까지로 임의로 정하고,
# 각 사람에 대한 불만도 계산
for i in range(0, len(lst)):
    y = abs(lst[i] - (i + 1))
    result+= y

print(result)