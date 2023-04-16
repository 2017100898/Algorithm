N = int(input())
A = input().split()

#  + / - / x / %
cmd = input().split()

A = [int(a) for a in A]
cmd = [int(a) for a in cmd]

min_value, max_value = 1e9, -1e9

# 모든 경우의 수를 고려하기 위해 함수를 만든다
def bf(idx, value, plus, minus, mul, div):
    global min_value, max_value
    
    # idx가 마지막 숫자를 가리킬 때는 이때까지의 최댓값/최솟값과 비교하여 업데이트한다.
    if idx + 1 == N:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
        return
    
    # 각 기호가 1 이상일 때, 조건에 따라 함수를 재귀한다
    if plus != 0:
        # 이때, value를 업데이트하고, 사용한 기호에 대해서 -1 해준다.
        bf(idx + 1, value + A[idx+1], plus - 1, minus, mul, div)
    if minus != 0:
        bf(idx + 1, value - A[idx+1], plus, minus - 1, mul, div)
    if mul != 0:
        bf(idx + 1, value * A[idx+1], plus, minus, mul - 1, div)
    if div != 0:
        bf(idx + 1, int(value / A[idx+1]), plus, minus, mul, div - 1)
        

bf(0, A[0], cmd[0], cmd[1], cmd[2], cmd[3])

print(max_value)
print(min_value)