lst = []
a = 0
b = 0

y = 0

# 9명의 키를 입력 받아서 list에 append 함
for i in range(0, 9):
    x = int(input())
    lst.append(x)
    # 모든 난쟁이의 합을 y에 저장함
    y+=x

# 찾아야할 두 난쟁이의 합을 구함
y = y - 100

# 2중 For 문을 통해 list를 정렬하는 과정
for i in range(0, len(lst)):
    for j in range(0, len(lst)):
        if lst[i] < lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

        # 정렬 하는 과정에서 비교하는 두 값의 합이 y일 때 Index를 체크해둠
        if lst[i] + lst[j] == y:
            a = lst[i]
            b = lst[j]

# 정렬한 list를 출력함. 이때, 찾아놓은 두 난쟁이는 출력하지 않음.
for i in range(0, 9):
    if lst[i] != a and lst[i] != b:
        print(lst[i])
