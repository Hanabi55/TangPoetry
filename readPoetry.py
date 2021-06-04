#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/5/10 20:11
@Author :Hanabi55
@File   :readPoetry.py
"""
f_read = open("全唐诗.txt", "r", encoding="utf-8")
f_write = open("poetry.txt", "a", encoding="utf-8")
for j in range(187770):
    poetryLine = []  # 用于存储每一行的诗句
    line = f_read.readline()
    while "，" in line and "。" in line:
        for i in line:
            if i != "\u3000" and i != "\n":
                poetryLine.append(i)
        line = f_read.readline()
    if len(poetryLine) != 0:
        strLine = ''.join(poetryLine)
        strLine = strLine + "\n"
        f_write.write(strLine)
f_read.close()
f_write.close()
