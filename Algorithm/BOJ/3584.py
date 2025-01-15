T = int(input())

def find_parent(x):
    result = [x]
    while parent[x]:
        result.append(parent[x])
        x = parent[x]
    return result

for _ in range(T):
    N = int(input())
    parent = [0 for i in range(N + 1)]

    for i in range(1, N + 1):
        parent[i] = []

    for _ in range(N - 1):
        # A, B : A가 B의 부모라는 뜻
        A, B = list(map(int, input().split()))
        parent[B] = A

    x, y = list(map(int, input().split()))

    x_parent = find_parent(x)
    y_parent = find_parent(y)

    i, j = 0, 0
    if len(x_parent) > len(y_parent):
        i = len(x_parent) - len(y_parent)
    else:
        j = len(y_parent) - len(x_parent)

    while x_parent[i] != y_parent[j]:
        i += 1
        j += 1

    print(x_parent[i])
    