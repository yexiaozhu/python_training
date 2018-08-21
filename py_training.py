#！ /usr/bin/env python 3.6.5
#coding = utf-8
#author = yexiaozhu

# 求输入数字平方，平方结果小于50，程序停止
def SQ(x):
    return x * x
print('如果平方结果小于50，程序停止')
again = 1
while again:
    num = int(input('请输入一个数字：'))
    print('运算结果：%d' %(SQ(num)))
    if SQ(num) < 50:
        again = 0