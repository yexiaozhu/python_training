#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，
# 闰年且输入月份大于2时需考虑多加一天：

# year = int(input('year:\n'))
# mouth = int(input('mouth:\n'))
# day = int(input('day:\n'))
#
# mouths = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < mouth <=12:
#     sum = mouths[mouth -1]
# else:
#     print('data error')
# sum += day
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 !=0)):
#     leap = 1
# if (leap == 1) and (mouth > 2):
#     sum += 1
# print('it is the %dth day.' %sum)

import time
D = input('请输入年份，格式XXXX-XX-XX：')
d = time.strptime(D, '%Y-%m-%d').tm_yday
print(d)
print(type(d))
print('the {} day of this year!'.format(d))