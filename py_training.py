#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

#题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

x1 = 1
l = []
for i in range(10):
    x2 = 2 * (x1 + 1)
    if i == 0:
        l.append(x1)
    else:
        x1 = x2
        l.append(x2)
print(l)
print(l[-1])gi