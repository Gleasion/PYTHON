from random import random
com = int(random()*99)+1
print("com",com)

flag_over = False
for i in range(10) :
    mine = input("(1~99)숫자를 하나 선택하세요")
    imine = int(mine)
    if com > imine :
        print("UP입니다.")
    elif com < imine :
        print("Down입니다.")
    else :
        print("정답입니다.")
        flag_over = True
        break

if not flag_over :
    print("Game over")