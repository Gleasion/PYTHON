from random import random

# 홀/짝을 선택하세요 홀
# 나: 홀
# 컴: 홀 짝
# 결과: 이김 짐

mine = ""
com = ""
result = ""

mine = input("홀/짝을 선택하세요")

rnd = random()
if rnd > 0.5 :
    com = "홀"
else :
    com = "짝"

if mine == com :
    result = "이김"
else :
    result = "짐"
    
print("나: {}".format(mine))
print("컴: {}".format(com))
print("결과: {}".format(result))
