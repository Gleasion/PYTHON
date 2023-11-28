from random import random
def getHollJack() :
    ret = "홀"
    rnd = random()
    if rnd > 0.5 :
        ret = "짝"
    return ret

com = getHollJack()
print("com", com)


    
