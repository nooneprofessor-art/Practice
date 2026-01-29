num = 0

def zoxa():
    global num
    num += 1
    print(num)
    num = 0
    zoma()

def zoma():
    global num
    player = int(input())
    num += player
    zoxa()
    
zoma()