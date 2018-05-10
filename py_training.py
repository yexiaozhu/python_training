#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
from sys import stdout

for i in range(2, 1001):
    k = []
    n = -1
    s = i
    for j in range(1, i):
        if i % j == 0:
            n += 1
            s -= j
            k.append(j)
    if s == 0:
        print(i)
        print(k)
        for i in range(n+1):
            # print(k[i])
            stdout.write(str(k[i]))
            stdout.write(' ')