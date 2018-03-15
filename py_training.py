#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
# 如果x>z则将x与z的值进行交换，这样能使x最小。

l = []
for i in range(3):
    x = int(input('输入第%d个整数：\n' %(i+1)))
    l.append(x)
l.sort()
print(l)