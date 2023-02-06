# 입력값을 받고, 피보나치 수를 저장할 리스트를 만듦.
N = int(input())
result = list()

# 리스트를 순회하며, index 가 0과 1일 때는 값을 넣어주고,
# 그보다 큰 값들에 대해서는 index i-1 과 i-2 의 값을 더해 새롭게 리스트에 값을 넣는다.
for i in range(0, N+1):
    if i == 0 or i == 1 :
        result.append(i)
    else:
        result.append(result[i-2] + result[i-1])
    
# N번째 index의 결과를 출력한다.
print(result[N])
