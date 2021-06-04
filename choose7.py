#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/5/10 21:10
@Author :Hanabi55
@File   :choose7.py
"""
f_read = open("poetry.txt", "r", encoding="utf-8")
f_write = open("poetry7.txt", "a", encoding="utf-8")
pakeage = []
x = 0
for i in range(43659):
    line = f_read.readline()
    if len(line) == 33 and "□" not in line and "（" not in line and "-" not in line and line[31]=="。":
        num_1 = 0
        num_2 = 0
        for j in line:
            if j == "，":
                num_1 += 1
            elif j == "。":
                num_2 += 1
        if num_1 + num_2 == 4 and line not in pakeage:
            x += 1
            if num_1 != 2:
                print(x)
            pakeage.append(line)
            f_write.write(line)
f_write.close()
f_read.close()
