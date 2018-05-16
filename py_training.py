#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 列表排序

def bubble(list):
    list_len = len(list)
    while list_len > 0:
        for j in range(list_len - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print('j:', j)
            print('list=', list)
        list_len -= 1
    # print('list=', list)
list = [1, 25, 15, 7, 10, 5]
#list = [1, 25]
bubble(list)