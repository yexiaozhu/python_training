#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

#题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。

sum = 0
t = 1
for i in range(1, 21):
    t *= i
    sum += t
print('20内阶乘之和：%d' %sum)