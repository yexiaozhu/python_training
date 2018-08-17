#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

#  题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

if __name__ == '__main__':
	# 最后一位0作为占位符
	a = [1,4,6,9,13,16,19,28,40,100,0]
	print('原始a:', a)
	for i in range(len(a)):
		print(a[i])
	number = int(input("\n插入一个数字；\n"))
	end = a[-2]
	if number > end:
		a[-1] = number
	else:
		for i in range(len(a)):
			if a[i] > number:
				a.insert(i, number)
				a.pop(-1)
				break
	print('排序后a', a)
