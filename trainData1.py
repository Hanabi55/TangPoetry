#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/30 8:14
@Author :Hanabi55
@File   :trainData2-1.py
"""
import random
from random import shuffle

f = open("poetry7.txt", "r", encoding="utf-8")
peomPackage = []
w_package = []
w_to_id = {' ': 0}
id_to_w = {0: ' '}

for j in range(7086):
    line = f.readline()
    peomPackage.append(line)
f.close()

for i in peomPackage:
    for j in i:
        if j not in w_package:
            w_package.append(j)

random.seed(10)
shuffle(w_package)

# print(len(w_package))

for i in range(len(w_package)):
    w_to_id[w_package[i]] = i
    id_to_w[i] = w_package[i]

x_train = []
y_train = []
x_test = []
y_test = []

for i in range(7086):
    list_tmp = []
    list_tmp1 = []
    for t in peomPackage[i]:
        list_tmp1.append(w_to_id[t])
    list_tmp = list_tmp1[16:32] + list_tmp1[0:16]
    if i < 3000:
        for j in range(1, 17):
            list_tmp_tmp = list_tmp[0:j + 15]
            while len(list_tmp_tmp) != 32:
                list_tmp_tmp.append(0)
            x_test.append(list_tmp_tmp)
            y_test.append(list_tmp[15 + j])
    else:
        for j in range(1, 17):
            list_tmp_tmp = list_tmp[0:j + 15]
            while len(list_tmp_tmp) != 32:
                list_tmp_tmp.append(0)
            x_train.append(list_tmp_tmp)
            y_train.append(list_tmp[15 + j])

# print(len(y_test),len(y_train))