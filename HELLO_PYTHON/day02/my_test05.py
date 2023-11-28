from random import random
num = list(range(1, 45+1))
print(num)

for i in range(1000) : 
    temp = num[0]
    rnd = int(random() * 45)
    num[0] = num[rnd]
    num[rnd] = temp

for j in range(1,6+1) :
    print(num[j])