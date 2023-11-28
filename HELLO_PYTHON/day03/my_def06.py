def add_min_mul_div(a,b):
    return a+b, a-b, a*b, a/b

sum = add_min_mul_div(4, 5)

# 튜플이 있는 단어는 multireturn 가능
# 작은 배열로 이해하면 됨
print("sum",sum)
print("sum",sum[2])
