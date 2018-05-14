#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：利用递归方法求5!。
# 递归公式：fn=fn_1*4!

def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j-1)
    return sum

print(fact(5))
print(fact(20))
