# 입력 받을 명령어의 개수를 입력 받음
N = int(input())

# Stack List
lst = list()

# 결과를 저장할 List
result = list()

# Push, 입력 값을 리스트의 가장 뒤에 넣어줌
def push(y):
    global lst
    lst.append(y)

# Top, -1 인덱스에 있는 숫자를 리턴함
# 이때, 리스트의 길이가 0이면 -1을 리턴함
def top():
    global lst
    if len(lst)==0:
        return -1
    else:
        return lst[-1]

# Size, 리스트의 length 리턴
def size():
    global lst
    return len(lst)
    
# Empty, 리스트의 길이가 0이면 1 리턴, 1이면 0을 리턴
def empty():
    global lst
    if len(lst) == 0:
        return 1
    else:
        return 0

# 리스트의 가장 마지막 인덱스 숫자를 없애고 리턴
# 리스트가 비어있을 때는 -1 리턴
def pop():
    global lst
    if len(lst) == 0:
        return -1
    else:
        return lst.pop()


for i in range(0, N):
    # 명령어를 입력 받음
    x = input()

    # 명령어의 앞 4자리가 push 일 때는 string 을 split하고, 
    # push 함수에 띄어쓰기 뒷 부분 (숫자)을 넣어줌
    if x[:4] == "push":
        x,y = x.split()
        push(y)

    # top, pop, empy, size에 대해서는 명령을 수행하고
    # 결과를 result list에 append
    elif x=="top":
        result.append(top())
    elif x == "pop":
        result.append(pop())
    elif x == "empty":
        result.append(empty())
    elif  x== "size":
        result.append(size())

# result 리스트를 순회하며 결과 출력
for j in result:
    print(j)

    
