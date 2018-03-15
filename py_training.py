#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：输出 9*9 乘法口诀表。
#
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# 题目：暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数。
import time

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d" %(i, j, i*j))
        time.sleep(1) # 暂停1秒