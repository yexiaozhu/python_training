#！ /usr/bin/env python 3.6.5
#coding = utf-8
#author = yexiaozhu

# 模仿静态变量(static)案例
# 演示一个python作用域使用方法

class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print('nNum = %d' %self.nNum)
        
if __name__ == "__main__":
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' %nNum)
        # inst = Num()
        inst.inc()