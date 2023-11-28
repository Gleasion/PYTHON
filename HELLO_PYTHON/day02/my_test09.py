from random import random

# 예시: 23
# (1~99) 숫자를 하나 선택하세요. 10
# UP입니다.
# (1~99) 숫자를 하나 선택하세요. 30
# DOWN입니다.
# (1~99) 숫자를 하나 선택하세요. 23
# 정답입니다.

# 10회 이상시 GAME OVER 띄우기

rnd = int(random()*99)+1
print(rnd)

for i in range(10):
    
    print(str(i) + "회")
    one = input("(1~99) 숫자를 하나 선택하세요.")
    a = int(one)
    
    if a < rnd :
        print("UP입니다.")
    elif a > rnd :
        print("DOWN입니다.")
    else :
        print("정답입니다.")
        break
    
    i += 1
    if i == 11 :
        print("GAME OVER")
        break