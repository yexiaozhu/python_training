#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input('请输入字符串：\n')
letters = 0
space = 0
number = 0
others = 0
for i in s:
    if i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    elif i.isalnum():
        number += 1
    else:
        others += 1

print('字符串中英文字母：%d，空格：%d，数字：%d，其他：%d' %(letters, space, number, others))
