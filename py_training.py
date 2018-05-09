#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

# 题目：输出指定格式的日期。
import time
from datetime import timedelta, datetime

date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# print(time.localtime(time.time()))
# print(date_time)
birthday = '1991-12-10 5:0:0'
# print(birthday)
birthday_time = time.strptime(birthday, '%Y-%m-%d %H:%M:%S')
print(type(birthday_time))
print(type(datetime.now()))
print(timedelta(days=5))
next_day = datetime.now() + timedelta(days=1)
print(next_day)