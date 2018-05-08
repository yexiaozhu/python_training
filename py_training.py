#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def reduceNum(n):
    print('{} = '.format(n))
    if not isinstance(n, int) or n <= 0:
        print('请输入正确数字:')
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:#循环保证递归
        for index in range(2, n+1):
            if n % index == 0:
                # print('index', index)
                # print('n', n)
                n = int(n/index)
                # print('n', n)
                if n == 1:
                    print(index)
                else:
                    print('{} *'.format(index))
                    break


reduceNum(100)

