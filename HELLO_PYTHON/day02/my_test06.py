# 출력할 구구단을 넣으세요(2~9) 2
# 2 * 1 = 2
# 2 * 2 = 4

# 2 * 9 =18

gugu = input("출력할 구구단을 넣으세요(2~9)")
dan = int(gugu)

for i in range(1, 9+1) :
    result = dan * i
    print("{} * {} = {}".format(dan,i,result))
    # print(dan + "*" + i + "=" + result)