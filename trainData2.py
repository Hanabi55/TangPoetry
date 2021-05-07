#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/27 13:37
@Author :Hanabi55
@File   :trainData.py
"""
"""code1
import random
from random import shuffle

f = open("peotry7.txt", "r", encoding="utf-8")
peomPackage = []
w_package = []
w_to_id = {}
id_to_w = {}

for j in range(6190):
    line = f.readline()
    peomPackage.append(line)
f.close()

for i in peomPackage:
    for j in i:
        if j not in w_package:
            w_package.append(j)

random.seed(10)
shuffle(w_package)
print(len(w_package))

for i in range(len(w_package)):
    w_to_id[w_package[i]] = i
    id_to_w[i] = w_package[i]

x_train = []
y_train = []
x_test = []
y_test = []

for i in range(len(peomPackage)):
    list_tmp = []
    for t in peomPackage[i]:
        list_tmp.append(w_to_id[t])
    if i < 1000:
        for j in range(16):
            x_test.append(list_tmp[j:j + 16])
            y_test.append(list_tmp[16 + j])
    else:
        for j in range(16):
            x_train.append(list_tmp[j:j + 16])
            y_train.append(list_tmp[16 + j])
        if i >= 3404:
            for j in range(16):
                x_train.append(list_tmp[32 + j:32 + j + 16])
                y_train.append(list_tmp[48 + j])

print("y_test:")
print(len(y_test))

"""

import random
from random import shuffle

f = open("peotry7.txt", "r", encoding="utf-8")
peomPackage = []
w_package = []
w_to_id = {' ': 0}
id_to_w = {0: ' '}

for j in range(6190):
    line = f.readline()
    peomPackage.append(line)
f.close()

for i in peomPackage:
    for j in i:
        if j not in w_package:
            w_package.append(j)

random.seed(10)
shuffle(w_package)

for i in range(len(w_package)):
    w_to_id[w_package[i]] = i
    id_to_w[i] = w_package[i]

x_train = []
y_train = []
x_test = []
y_test = []

for i in range(6190):
    list_tmp = []
    for t in peomPackage[i]:
        list_tmp.append(w_to_id[t])
    if i < 3404:
        for j in range(1, 17):
            list_tmp_tmp = list_tmp[0:j + 15]
            while len(list_tmp_tmp) != 32:
                list_tmp_tmp.append(0)
            x_test.append(list_tmp_tmp)
            y_test.append(list_tmp[15 + j])
    else:
        list_tmp1 = list_tmp[0:16] + list_tmp[16:32]
        for j in range(1, 17):
            list_tmp_tmp = list_tmp1[0:j + 15]
            while len(list_tmp_tmp) != 32:
                list_tmp_tmp.append(0)
            x_train.append(list_tmp_tmp)
            y_train.append(list_tmp1[15 + j])
        list_tmp1 = list_tmp[32:48] + list_tmp[48:64]
        if i >= 3404:
            list_tmp_tmp = list_tmp1[0:j + 15]
            while len(list_tmp_tmp) != 32:
                list_tmp_tmp.append(0)
            x_train.append(list_tmp_tmp)
            y_train.append(list_tmp1[15 + j])
