from itertools import product

N = int(input())
test_case = []

for i in range(N):
    n = int(input())
    test_case.append(n)

# +나 -, 공백을 숫자 사이에 삽입해서 그 결과가 0이 될 수 있는지 살펴보자!
# 각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 수식을 출력
# 공백, + , -

cal_set = [" ", "+", "-"]

for i in test_case:
    num_set = [num + 1 for num in range(i)]
    num_len = i - 1
    cal_list = product(cal_set, repeat = num_len)
    
    for cal in cal_list:
        cal = list(cal)
        res_list = ["1"]

        for j in range(len(cal)):
            if cal[j] == ' ':
                res_list[-1] = res_list[-1] + str(j + 2)
            
            elif cal[j] == '+':
                res_list.append(str(j +  2))
            
            else:
                res_list.append(str(-1 * (j + 2)))

        res_num = 0

        for k in range(len(res_list)):
            res_num += int(res_list[k])
        #print(res_list)
        
        
        if res_num == 0:
            
            for m in range(len(cal)):
                print(m + 1, end="")
                print(cal[m], end= "")

            print(len(cal)+ 1)
    
    print()
