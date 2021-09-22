# -*- encoding: utf-8 -*-
"""
@Project ：Flash_Drought_Research 
@File    : function_d.py
@Software: PyCharm
@Time    : 2021/7/29 18:31
@Author  : WANG YAO
Annotation : this is for testing uploading files
"""
import pandas as pd
import numpy as np
import datetime
import time


def ridoferror(p):
    l = len(p)
    for k in range(l):
        if p[k] == 32700:
            p[k] = 0
    return p


def get3mx(p):
    l = len(p)
    mx3 = 0
    for k in range(0, l - 2):
        mx = sum(p[k:k + 2])
        if mx > mx3:
            mx3 = mx
        else:
            mx3 = mx3
    return mx3


def get5mx(p):
    l = len(p)
    mx5 = 0
    for k in range(0, l - 4):
        mx = sum(p[k:k + 4])
        if mx > mx5:
            mx5 = mx
        else:
            mx5 = mx5
    return mx5


def double_v(p):
    l = len(p)
    list_0_1 = []
    for i in range(l):
        if p[i] > 0:
            list_0_1.append(1)
        else:
            list_0_1.append(0)
    return list_0_1


def RLC(p):
    l = len(p)
    position = []
    number = []

    for k in range(0, l - 1):
        if p[k + 1] != p[k]:
            position.append(k + 1)
            number.append(p[k])
    number.append(p[-1])
    RLCp = list(range(0, len(position) + 1))
    print(RLCp, position)
    if position:
        RLCp[0] = position[0]

        for j in range(1, len(position)):
            RLCp[j] = position[j] - position[j - 1]
        RLCp[-1] = l - position[-1]

        RLC_series = []
        for n in range(len(RLCp)):
            RLC_series.append((number[n], RLCp[n]))
    else:
        RLC_series = [(0, len(p))]

    return RLC_series


def cdd(p):
    l = len(p)
    cont_d = 0
    cont_xd = 0
    for i in range(l):
        if p[i][0] == 0:
            cont_xd = p[i][1]
        if cont_xd > cont_d:
            cont_d = cont_xd
    return cont_d


def cwd(p):
    l = len(p)
    cont_w = 0
    cont_xw = 0
    for i in range(0, l):
        if p[i][0] == 1:
            cont_xw = p[i][1]
        if cont_xw > cont_w:
            cont_w = cont_xw
    return cont_w


# sample
#p = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#      1, 1, 1, 1]
# pp = RLC(p)
# print(pp)
# print(pp[1][1])
# pp[1][1]  # [(0, 7), (1, 4), (0, 3), (1, 7), (0, 2), (1, 3), (0, 1), (1, 1), (0, 1), (1, 13)]
# a = cdd(pp)
# print(a)
# b = cwd(pp)
# print(b)
# position = [1]
# if position:
#     print(1)
# else:
#     print(0)
