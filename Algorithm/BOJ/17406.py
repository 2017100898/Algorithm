from itertools import permutations
from copy import deepcopy

N, M, K = list(map(int, input().split()))

# 배열 A
A = []
for _ in range(N):
    min_A = list(map(int, input().split()))
    A.append(min_A)

# 회전 정보
rotate = []
for _ in range(K):
    min_rot = list(map(int, input().split()))
    rotate.append(min_rot)

# A의 최소값 계산 함수
def calc_val_A(mat):
    row_val = 9999999

    for row_mat in mat:
        if row_val > sum(row_mat):
            row_val = sum(row_mat)

    return row_val


def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j] , end = " ")
        print()
    print()


# A 회전 함수
def rotate_A(mat, rcs_perm):
    
    for rcs in rcs_perm:
        new_mat = deepcopy(mat)

        r, c, s = rcs[0], rcs[1], rcs[2]
        s_i_a, s_j_a = r - s - 1, c - s - 1
        e_i_a, e_j_a = r + s - 1, c + s - 1 # 기준점 설정
        lim = s * 2

        for n in range(s):
            
            s_i = s_i_a + n
            s_j = s_j_a + n
            e_i = e_i_a - n
            e_j = e_j_a - n

            for k in range(lim):
                mat[s_i][s_j + k + 1] = new_mat[s_i][s_j + k]

            for k in range(lim):
                mat[e_i][e_j - k - 1] = new_mat[e_i][e_j - k]

            for k in range(lim):
                mat[s_i + k + 1][e_j] = new_mat[s_i + k][e_j]

            for k in range(lim):
                mat[e_i - k - 1][s_j] = new_mat[e_i - k][s_j]

            #print_mat(mat)

            lim -= 2
    return mat


    

# permutation 경우의 수
perms = permutations(rotate)
min_val = 99999999

for perm in perms:
    sub_A = deepcopy(A)
    rotated_mat = rotate_A(sub_A, perm)
    val = calc_val_A(rotated_mat)
    if min_val > val:
        min_val = val

print(min_val)