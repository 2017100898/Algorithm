N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))
prefix_sum = [0]

for i in range(N):
    prefix_sum.append(prefix_sum[-1] + arr[i])


if N == K:
    print(prefix_sum[-1])

else:
    max_val = -9999999999999

    for i in range(K, N + 1):
        diff = prefix_sum[i] - prefix_sum[i - K]
        max_val = max(diff, max_val)

    print(max_val)