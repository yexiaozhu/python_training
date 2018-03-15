#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

l = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (k != i):
                l.append([i, j, k])
                print(len(l), i, j, k)