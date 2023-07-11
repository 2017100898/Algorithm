N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
cnt = 0
result = -1

def merge_sort(A):
    if len(A) <= 1 : 
        return A
    
    mid = (len(A) + 1) // 2
    left = A[:mid]
    right = A[mid:]

    res_left = merge_sort(left)
    res_right = merge_sort(right)

    return merge(res_left, res_right)

def merge(left, right):
    global result, cnt

    i, j, k = 0, 0, 0
    sorted = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    
    while i < len(left) :
        sorted.append(left[i])
        i += 1

    while j < len(right):
        sorted.append(right[j])
        j += 1
    
    while k < len(sorted):
        cnt += 1

        if cnt == K:
            result = sorted[k]

        k += 1
    
    return sorted

merge_sort(A)
print(result)