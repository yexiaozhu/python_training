#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：按逗号分隔列表。

l = [1, 2, 3, 4, 5]
s = 0
s = ','.join(str(i) for i in l)
print(s)