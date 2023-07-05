# 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다
# 없어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게되면 또 터지게 된다
# 내려오고 터짐을 반복하면서 1연쇄씩 늘어난다
from collections import deque

fields  = []
results = 0
again = 2


for i in range(12):
    field = list(input())
    fields.append(field)

# 아래 두 태스크의 반복
queue = deque([])

# 상하좌우로 연결되어 있는 것 찾기
while True:
    again = 0
    remove = []

    for i in range(12):
        for j in range(6):
            values = []
            value = fields[i][j]
            cnt  = 1
            
            if value != ".":    
                queue.append((i, j))
                values.append((i, j))

            while len(queue) != 0 :
                ab = queue.pop()
                a, b = ab[0], ab[1]
                
                if a != 11 and (a + 1, b) not in values:
                    if fields[a + 1][b] == value:
                        queue.append((a + 1, b))
                        values.append((a + 1, b))
                        cnt+=1

                if a != 0 and (a - 1, b) not in values:
                    if fields[a - 1][b] == value:
                        queue.append((a - 1, b))
                        values.append((a - 1, b))
                        cnt+=1

                if b != 5 and (a, b + 1) not in values:
                    if fields[a][b + 1] == value:
                        queue.append((a, b + 1))
                        values.append((a, b + 1))
                        cnt+=1

                if b != 0 and (a, b - 1) not in values:
                    if fields[a][b - 1] == value:
                        queue.append((a, b - 1))
                        values.append((a, b - 1))
                        cnt+=1

            if cnt >= 4:
                for val in values:
                    remove.append(val)
                again = 1

    if again == 1:
        for val in remove:
            k, m = val[0], val[1]
            fields[k][m] = "."
        results +=1

    elif again != 1:
        break
    
# 삭제된 공간 채우기
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if fields[j][i] != "." and fields[k][i] == ".":
                    fields[k][i] = fields[j][i]
                    fields[j][i] = "."

    
print(results)
