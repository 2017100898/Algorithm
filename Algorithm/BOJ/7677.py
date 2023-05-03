while True:
    N = int(input())
    if N == -1:
        break
    else:
        x = [[1, 1], [1, 0]]

        def mul(A, B):
            N = len(A)
            c = [[0] * N for _ in range(N)]
            # 행 순회
            for i in range(N):
                # 열 순회
                for j in range(N):
                    for k in range(N):
                        c[i][j] += A[i][k] * B[k][j] % 10000

            return c

        # 분할정복을 위해 사용하는 함수
        def power(A, N):
            if N == 0 :
                return [[0, 0], [0,0]]
            
            elif N == 1:
                return A
            
            a = power(A, N // 2)

            if N % 2 == 0:
                return mul(a , a)
            
            else:
                return mul(mul(a, a), A)
            
        result = power(x, N)

        print(result[0][1] %  10000)