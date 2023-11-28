# 첫수를 입력하시오 5
# 끝수를 입력하시오 7
# 5에서 7까지의 합은 18입니다.

a = input("첫수를 입력하시오")
b = input("끝수를 입력하시오")
# arr = range(int(a), int(b)+1)
# c = sum(list(arr))
# print("{}에서 {}까지의 합은 {}입니다.".format(a,b,c))

aa = int(a)
bb = int(b)
sum = 0
for i in range(aa,bb+1):
    sum += i
    
print("{}에서 {}까지의 합은 {}입니다.".format(a,b,sum))
