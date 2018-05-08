#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for number in range(100, 1000):
    number_hundreds = int(number / 100)
    number_ten = int(number / 10 % 10)
    number_one = int(number % 10)
    # print(number_one, number_ten, number_hundreds)
    if number == number_hundreds ** 3 + number_ten ** 3 + number_one ** 3:
        # print(number)
        print('水仙花数', number)