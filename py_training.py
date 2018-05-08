#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 判断101-200之间有多少个素数，并输出所有素数。
# 质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
import logging
from math import sqrt

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
leap = 1
h = 0
prime_list = []
numbers = range(101, 201)
for m in range(101, 201):
    k = int(sqrt(m + 1))
    for i in range(2, k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print(m)
        prime_list.append(m)
        h += 1
    leap = 1

print(len(prime_list))