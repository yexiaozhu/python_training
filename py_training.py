#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

s1 = input('请输入首字母：')
if s1 == 'S':
    s2 = input('请输入次字母：')
    if s2 == 'a':
        print('Saturday')
    elif s2 == 'u':
        print('Sunday')
    else:
        print('data error')

elif s1 == 'F':
    print('Friday')

elif s1 == 'M':
    print('Monday')

elif s1 == 'T':
    print('please input second letter')
    s2 = input("please input:")

    if s2 == 'u':
        print('Tuesday')
    elif s2 == 'h':
        print('Thursday')
    else:
        print('data error')

elif s1 == 'W':
    print('Wednesday')
else:
    print('data error')