


'''
4 x 4 크기의 공간, 1 x 1 크기의 정사각형으로 나누어져 있음
한칸에 물고기 한마리 존재

각 물고기는 번호와 방향 가지고 있음. (번호는 1보다 크거나 같고, 16보다 작은 자연수)
두 물고기가 같은 번호 가지는 경우는 X

[초기 설정]
청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어감
상어의 방향은 기존의 (0, 0)에 있던 물고기의 방향과 같음. 
이후 물고기가 이동

[물고기의 이동]
번호가 작은 물고기부터 순서대로 이동
물고기는 한 칸 이동 할 수 있음.
이동할 수 있는 칸 : 빈칸, 다른 물고기가 있는 칸
                다른 물고기가 있는 칸으로 이동할 경우, 그 물고기와 자리 바꿈

이동 불가능 : 상어가 있거나, 공간의 경계를 넘는 칸
              이동을 할 수 있을 때까지 방향을 45도 반시계 방향으로 회전한다
              그렇게 해도 이동할 수 있는 칸이 없으면... 이동 안함

[상어의 이동]
물고기의 이동이 모두 끝나면 상어가 이동
방향에 있는 칸으로 이동 가능
1. 한번에 여러 칸 이동 가능. 
2. 상어가 물고기가 있는 칸으로 이동하면, 그 물고기 먹고, 그 물고기의 방향 갖게 됨
3. 지나가는 칸에 있는 물고기는 먹지 않음
4. 이동할 수 있는 칸이 없으면 집으로 감

'''



################## Fish Class
import copy


class fish:
    def __init__(self):
        self.direct = None
        self.num = None
        self.is_shark = False
        self.eat_num = 0
    
    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num
    
    def set_direct(self, num):
        self.direct = num

    def get_direct(self):
        return self.direct
    
    def get_direct_detail(self):
        direct_list = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        return direct_list[self.direct - 1]
    
    def rotate_direct(self):
        direct_list = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        
        if self.direct == 8:
            self.direct = 1
        else:
            self.direct += 1

        return direct_list[self.direct - 1]
    
    def eat(self, fish):
        if self.is_shark == True:
            #print(f"EAT {fish.get_num()}")
            self.eat_num += fish.get_num()
            self.set_direct(fish.get_direct())
            self.set_num(-1)

        return self.eat_num

    def print_eat_num(self):
        return self.eat_num
    
    def shark(self):
        self.is_shark = True

##################### 정보 입력 받고, arr 만들기
init_arr = []
fish_set = [i for i in range(1, 17)]

for i in range(4):
    info = list(map(int, input().split()))
    temp_arr = []

    for j in range(0, 8, 2):
        num  = info[j]
        direct = info[j + 1]

        fs = fish()
        fs.set_direct(direct)
        fs.set_num(num)

        temp_arr.append(fs)

    init_arr.append(temp_arr)

def print_arr(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == None:
                print("N", end= " ")
            else:
                print(arr[i][j].get_num(), end = " ")
        print()
    print()
            


def can_go(arr, nx, ny):
    if nx not in range(4):
        return False
    
    elif ny not in range(4):
        return False
    
    elif arr[nx][ny] == None:
        return True

    elif arr[nx][ny].get_num() == -1:
        return False
    
    else:
        return True


def can_go_shark(arr, nx, ny):
    if nx not in range(4):
        return False
    
    elif ny not in range(4):
        return False
    
    elif arr[nx][ny] == None:
        return False

    elif arr[nx][ny].get_num() == -1:
        return False
    
    else:
        return True




#################### 잡아먹기와 이동 시작
        
############## 초기, (0, 0) 잡아먹음
shark = fish()
shark.shark()

fish_set.remove(init_arr[0][0].get_num())
shark.eat(init_arr[0][0])
init_arr[0][0] = shark

shark_dest = (0, 0)
#print("***************")
#print_arr(init_arr)

max_v = 0

def move(shark_dest, arr, fish_set):
    global max_v
    #print(shark_dest)
    arr = copy.deepcopy(arr)
    shark_dest = copy.deepcopy(shark_dest)
    fish_set = copy.deepcopy(fish_set)

    ############## 물고기 이동
    
    for k in range(len(fish_set)):
        next_fish = False

        for x in range(4):
            if next_fish == True:
                break

            for y in range(4):
                fs = arr[x][y]

                if fs != None:
                    fs_num = fs.get_num()

                    if fs_num == fish_set[k]:
                        rotate_num = 0
                        dx, dy = fs.get_direct_detail()
                        nx = dx + x
                        ny = dy + y

                        while can_go(arr, nx, ny) == False and rotate_num < 8:
                            dx, dy = fs.rotate_direct()
                            nx = dx + x
                            ny = dy + y
                            rotate_num += 1

                        if can_go(arr, nx, ny):
                            if arr[nx][ny] == None: ########### 이동 가능한 곳이 빈곳이라면
                                arr[nx][ny] = fs
                                arr[x][y] = None

                            else: ############### 이동 가능한 곳에 물고기가 있다면 
                                    temp = arr[nx][ny] ########자리바꿈
                                    arr[nx][ny] = fs
                                    arr[x][y] = temp
                            
                            next_fish = True
                            break

                        else:
                            next_fish = True
                            break
                                       
    ####### 상어의 이동

    shark_x, shark_y = shark_dest
    dx, dy = arr[shark_x][shark_y].get_direct_detail()

    stopped = False
    for i in range(1, 4):
        nx = shark_x + (dx * i)
        ny = shark_y + (dy * i)

        if can_go_shark(arr, nx, ny):
            stopped = True
            
            temp_arr = copy.deepcopy(arr)
            temp_fish_set = copy.deepcopy(fish_set)
            temp_shark_x = copy.deepcopy(shark_x)
            temp_shark_y = copy.deepcopy(shark_y)
            fs = temp_arr[nx][ny]
            fs_num = fs.get_num()
            
            temp_fish_set.remove(temp_arr[nx][ny].get_num())
            temp_arr[temp_shark_x][temp_shark_y].eat(temp_arr[nx][ny])
            temp_arr[nx][ny] = temp_arr[temp_shark_x][temp_shark_y]
            temp_arr[temp_shark_x][temp_shark_y] = None
            
            move((nx, ny), temp_arr, temp_fish_set)
            
    if stopped != True:
        max_v = max(max_v, arr[shark_x][shark_y].print_eat_num())
        return
    
move(shark_dest, init_arr, fish_set)

print(max_v)