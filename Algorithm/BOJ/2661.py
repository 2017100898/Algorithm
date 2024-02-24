n = int(input())
answer = []
fin  = False

def is_good():
    for i in range(2, len(answer) // 2 + 1):
        a = answer[-i:]
        b = answer[-i * 2:-i]
        
        if a == b:
            return False

    return True
        
def print_answer():
    for elem in answer:
        print(elem, end="")
    print()
        
def choose(curr_num):
    global fin
    
    if is_good():
        if fin == True : 
            return

        if curr_num == n:
            print_answer()
            fin = True
            return

        for i in range(1, 4):
            if len(answer) == 0:
                answer.append(i)
                choose(curr_num + 1)
                answer.pop()
            
            elif len(answer) >= 1 and answer[-1] != i:
                answer.append(i)
                choose(curr_num + 1)
                answer.pop()

choose(0)
