#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/29 10:57
@Author :Hanabi55
@File   :main.py
"""
from createDict import id_to_w, w_to_id
from model1_use import create1_2
from model2_use import create3_4

inputPeom = []
result = []
inputPeom_w = input("输入两句例诗：")
for i in inputPeom_w:
    inputPeom.append(w_to_id[i])
print("这两句诗是原诗前两句还是后两句:")
tmp = int(input("1:前两句\n2:后两句\n请选择:"))
print("是否要进行训练，需要则输入训练次数，不需要输入0：")
num_epochs = int(input())
if tmp == 1:
    peom2 = create3_4(num_epochs, inputPeom)
    inputPeom = [] + peom2
    peom1 = create1_2(num_epochs, inputPeom)
elif tmp == 2:
    peom1 = create1_2(num_epochs, inputPeom)
    inputPeom = [] + peom1
    peom2 = create3_4(num_epochs, inputPeom)
result = peom1 + peom2
print("生成唐诗：")
for i in result:
    print(id_to_w[i], end='')
