#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：暂停一秒输出，并格式化当前时间。

import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

time.sleep(1) # 暂停1秒

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))