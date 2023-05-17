N = int(input())
regex = input()
# 정규표현식을 *를 기준으로 쪼갠다.
regex = regex.split("*")

# 문자열을 입력받을 때마다 정규표현식과 비교하는 과정을 거친다.
for i in range(0, N):
    word = input()

    # regex[0]과 입력받은 문자열의 regex[0] 길이 만큼의 앞 부분 sub-string과 같은지 비교한다.
    if word[0 : len(regex[0])] == regex[0]:
        # 비교한 부분은 삭제를 해준다.
        word = word[len(regex[0]):]
        
        # regex[1]과 입력받은 문자열의 regex[1] 길이 만큼의 뒷 부분 sub-string과 같은지 비교한다.
        if word[-len(regex[1]):] == regex[1]:
            print("DA")
        else:
            print("NE")

    else:
        print("NE")
