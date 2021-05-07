#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/22 21:40
@Author :Hanabi55
@File   :dataset.py
"""

"""
f_write = open("peotry7.txt","a",encoding="utf-8")
try:
    i = 1
    while True:
        filename="poetry7_4/"+str(i)+".txt"
        f_read = open(filename,"r",encoding="utf-8")
        line = f_read.readline()
        strLine = ''.join(line)
        strLine = strLine + "\n"
        f_write.write(strLine)
        f_read.close()
        i+=1
except:
    pass
try:
    i = 1
    while True:
        filename="poetry7_8/"+str(i)+".txt"
        f_read = open(filename,"r",encoding="utf-8")
        line = f_read.readline()
        strLine = ''.join(line)
        strLine = strLine + "\n"
        f_write.write(strLine)
        f_read.close()
        i+=1
except:
    pass
f_write.close()
"""

"""
f=open("peotry7.txt","r",encoding="utf-8")
try:
    i = 1
    while True:
        line = f.readline()
        line1 = line[0:7]
        line2 = line[8:15]
        line3 = line[16:23]
        line4 = line[24:31]
        if "，"in line1 or "，"in line2 or "，"in line3 or "，"in line4:
            print(i)
        i+=1
except:
    pass
f.close()
"""
"""
f = open("peotry7.txt", "r", encoding="utf-8")
for i in range(1,6198):
    line = f.readline()
    if i > 3409:
        line_5 = line[32:39]
        line_6 = line[40:47]
        line_7 = line[48:55]
        line_8 = line[56:63]
        if "，" in line_5 or "，" in line_6 or "，" in line_7 or "，" in line_8:
            print(i)
f.close()
"""
"""
f=open("peotry7.txt","r",encoding="utf-8")
f_all=[]
f_all_dict={}
for i in range(6196):
    line = f.readline()
    if line in f_all:
        print(f_all_dict[line],i+1)
    else:
        f_all_dict[line]=i+1
        f_all.append(line)
"""
"""
f = open("peotry7.txt", "r", encoding="utf-8")
for i in range(6199):
    line = f.readline()
    if "□" in line:
        print(i+1)
"""
"""
from peomData import x_train,y_train

print("x_train:",len(x_train))
print("y_train:",len(y_train))
"""
"""
import tensorflow as tf

a=tf.constant([1,2,3,4])
a1=a[:1]
a2=a[2:]
a3=tf.constant([0])
a4=tf.concat([a1,a3,a2],axis=1)
print(a4)
"""
"""
f = open("peotry7.txt", "r", encoding="utf-8")
for i in range(6190):
    line = f.readline()
    if "不" in line:
        print(i+1)
"""
"""
import tensorflow as tf
import os
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
print(os.environ['CUDA_VISIBLE_DEVICES'])
"""
import tensorflow
print(tensorflow.test.is_gpu_available())