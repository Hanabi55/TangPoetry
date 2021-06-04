#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/29 10:57
@Author :Hanabi55
@File   :main.py
"""
from createDict import id_to_w, w_to_id,peomPackage
from model1_use import create1_2
from model2_use import create3_4
from createPeom import createPeom,wordToid
import random


random.seed(random.randint(1, 100))

while True:
    user = int(input("请选择功能：\n输入'0'结束功能\n输入'1'进行训练\n输入'2'开始生成唐诗\n请输入你的选择:"))
    if user == 0:
        break
    elif user == 1:
        trainNum = int(input("请输入训练次数:"))
        str1="朝辞白帝彩云间，千里江陵一日还。"
        str2="两岸猿声啼不住，轻舟已过万重山。"
        create1_2(num_epochs=trainNum,inputPeom=wordToid(list(str2)))
        create3_4(num_epochs=trainNum,inputPeom=wordToid(list(str1)))
        print("训练结束")
    elif user == 2:
        createNum = int(input("请输入生成诗的数量:"))
        for i in range(createNum):
            createPeom()
        print("编写结束")