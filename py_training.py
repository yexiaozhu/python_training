#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

number = 0
number_list = []
n = int(input('n='))
a = int(input('a='))
for i in range(n):
    number = number + a
    a = a * 10
    print(number)
    number_list.append(number)

number_total = sum(number_list)
print('总和：%d' % number_total)