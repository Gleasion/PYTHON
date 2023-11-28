# 야구 게임
# 1~9의 숫자 중 세 개의 숫자를 중복 없이 고른다.
# com = "234"
# 세 숫자를 입력 하세요 : 123
# 0S2B
# 세 숫자를 입력 하세요 : 234
# 3S 3B
# 축하합니다

from random import random

com = "123"

def ranC():
    arr = [1,2,3,4,5,6,7,8,9]
    for i in range(100):
        rnd = int(random()*9)
        a = arr[0]
        arr[0]=arr[rnd]
        arr[rnd]=a
    com = "{}{}{}".format(arr[0],arr[1],arr[2])
    print("com",com)
    return com
    
def getS(mine, com):
    ret = 0
    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]

    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]
    
    if m1 == c1 : ret+=1
    if m2 == c2 : ret+=1
    if m3 == c3 : ret+=1
    
    return ret

def getB(mine, com):
    
    ret = 0
    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]

    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]
    
    if m1 == c2 or m1 == c3 : ret+=1
    if m2 == c1 or m2 == c3 : ret+=1
    if m3 == c1 or m2 == c2 : ret+=1
    
    return ret

com = ranC()
while True:
    mine = input("1~9 사이의 세가지의 숫자를 입력하세요")
    s = getS(mine, com)
    b = getB(mine, com)
    print(mine,"s"+str(s),"b"+str(b))
    if s == 3 :
        print("정답입니다.")
        break