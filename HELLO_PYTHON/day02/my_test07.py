# 첫수를 입력하세요 1
# 끝수를 입력하세요 10
# 배수를 입력하세요 5
# 1에서 10까지의 5의 배수의 합은 15입니다.

first = input("첫수를 입력하세요")
last = input("끝수를 입력하세요")
bae = input("배수를 입력하세요")

a = int(first)
b = int(last)
c = int(bae)

sum = 0
for i in range(a, b+1) :
    if i % c == 0 :
        sum += i

print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(a,b,c,sum))
