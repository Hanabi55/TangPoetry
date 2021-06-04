#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/27 13:37
@Author :Hanabi55
@File   :trainData.py
"""
from createDict import w_to_id, id_to_w, peomPackage

x_train = []
y_train = []
x_test = []
y_test = []

for i in range(7086):
    list_tmp = []
    for t in peomPackage[i]:
        list_tmp.append(w_to_id[t])
    if i < 1000:
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
