# 가위/바위/보를 선택하세요
# 나 : 가위
# 컴 : 가위
# 결과 : 비김 
from random import random

me = input("가위/바위/보를 선택하세요.")

arr = ["가위","바위","보"]
for i in range(1000) :
    temp = arr[0]
    rnd = int(random() * 3)
    arr[0] = arr[rnd]
    arr[rnd] = temp

com = arr[0]

print("나: " + me)
print("컴: " + com)

if (me == "가위" and com == "바위") or (me == "바위" and com == "보") or (me == "바위" and com == "보") :
    print("나 이김")
elif (me == "가위" and com == "바위") or (me == "바위" and com == "보") or (me == "바위" and com == "보") :
    print("나 짐")
else : 
    print("비김")