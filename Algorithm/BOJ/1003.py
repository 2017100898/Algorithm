T = int(input())
zero = [0 for _ in range(41)]
one = [0 for _ in range(41)]
zero[0] = 1
one[1] = 1

for i in range(T):
    t = int(input())

    for i in range(2, t+1):
        if zero[i] == 0 and one[i] == 0:
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
        else:
            pass

    print(f"{zero[t]} {one[t]}")