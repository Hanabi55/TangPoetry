#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/5/11 16:33
@Author :Hanabi55
@File   :createDict.py
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
