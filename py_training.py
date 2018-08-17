#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。
 
if __name__ == '__main__':
	a = [9,6,5,4,1]
	N = len(a)
	print(a)
	for i in range(int(N / 2)):
		a[i], a[N - i -1] = a[N - i - 1], a[i]
	print(a)