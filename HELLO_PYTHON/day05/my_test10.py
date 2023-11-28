# 첫별수를 입력하시오 5
# 끝별수를 입력하시오 7

# *****
# ******
# *******

def drawStar(cnt):
    ret = ""
    for i in range(cnt):
        ret += "*"
    ret += "\n"
    return ret

a = input("첫별수를 입력하시오")
b = input("끝별수를 입력하시오")
aa = int(a)
bb = int(b)

str = ""

for i in range(aa,bb+1):
    str += drawStar(i)

print(str)