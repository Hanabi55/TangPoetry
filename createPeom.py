#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/5/14 1:44
@Author :Hanabi55
@File   :createPeom.py
"""
from createDict import id_to_w, w_to_id, peomPackage
from model1_use import create1_2
from model2_use import create3_4
import random


def wordToid(inputPeom_w_tmp):
    inputPeom_tmp = []
    for i in inputPeom_w_tmp:
        inputPeom_tmp.append(w_to_id[i])
    return inputPeom_tmp


def idToWord(result_tmp):
    result_w_tmp = []
    for i in result_tmp:
        result_w_tmp.append(id_to_w[i])
    return result_w_tmp


def createPeom():
    f_write = open("poetry_create.txt", "a", encoding="utf-8")
    peom1 = []
    peom2 = []
    inputPeom = []
    inputPeom_w = []
    result = []
    result_w = []
    tmp = random.randint(1, 2)
    peom_x = random.randint(0, 1000)
    inputPeom_w_all = peomPackage[peom_x]
    if tmp == 1:
        inputPeom_w = inputPeom_w_all[0:16]
        inputPeom = wordToid(inputPeom_w)
        peom2 = create3_4(0, inputPeom)
        inputPeom = [] + peom2
        peom1 = create1_2(0, inputPeom)
    elif tmp == 2:
        inputPeom_w = inputPeom_w_all[16:32]
        inputPeom = wordToid(inputPeom_w)
        peom1 = create1_2(0, inputPeom)
        inputPeom = [] + peom1
        peom2 = create3_4(0, inputPeom)
    result = peom1 + peom2
    result_w = idToWord(result)
    result_w.append('\n')
    result_w_str = ''.join(result_w)
    f_write.write(result_w_str)
    f_write.close()
    return 0
