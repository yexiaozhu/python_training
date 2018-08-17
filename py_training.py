#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
if __name__ == '__main__':
	a = []
	sum = 0.0
	for i in range(3):
		# print('a:', a)
		a.append([])
		for j in range(3):
			a[i].append(float(input("input num:\n")))
	for k in range(3):
		sum += a[k][k]
	print('a:', a)
	print('sum:', sum)