# 입력값을 받아서 list로 변환함
y = list(input())

# 2중 For문을 통한 리스트 정렬
for i in range(0, len(y)):
    for j in range(0, len(y)):
        if y[i] > y[j]:
            temp = y[i]
            y[i] = y[j]
            y[j] = temp

# list를 string으로 변환하여 출력
y = "".join(y)
print(y)

