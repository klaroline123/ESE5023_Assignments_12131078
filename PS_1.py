# -*- encoding: utf-8 -*-
"""
@Project ：Assignment_1
@File    : HW1.py
@Tutor   : ZHU LEI
@Time    : 2021/9/22 17:03
@Author  : WANG YAO
Annotation :
"""
import random
import numpy as np


def Print_values():  # Q1
    a = np.random.randint(1, 100)
    b = np.random.randint(1, 100)
    c = np.random.randint(1, 100)
    if a > b:
        if b > c:
            print(a, b, c)
        elif a > c:
            print(a, c, b)
        else:
            print(c, a, b)
    else:
        if b > c:
            print('b cannot be the max according to the requirement')
        else:
            print(c, b, a)


def Matrix_multip():  # Q2
    def point_multy(a, b):
        # a and b are vectors with same size
        length: int = len(a)
        c = np.zeros(length)
        for n in range(length):
            c[n] = a[n] * b[n]
        s = sum(c)
        return s

    M1 = np.random.randint(0, 50, size=(5, 10))
    M2 = np.random.randint(0, 50, size=(10, 5))
    L = 5
    M3 = np.zeros((5, 5))
    for i in range(L):
        for j in range(L):
            M3[i, j] = point_multy(M1[i, :], M2[:, j])
    print(M1, M2, M3)
    return M3


def Pascal_triangle(MaxLine):  # Q3

    N = [1]
    cont = 1
    while cont <= MaxLine:
        cont = cont + 1
        S = N[:]
        S.append(0)
        N = [S[i - 1] + S[i] for i in range(len(S))]
        if cont == MaxLine:
            print(N)

    return N


def Least_moves(n):  # Q4
    step = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            step = step + 1
        else:
            n = n - 1
            step = step + 1
    print(step)

    return step


def Find_expression(Max_values):  # q5

    init_sq = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def ten2ter(nn):
        def ternary(n):  # 这里把n转换为3进制数字，0表示空，1表示+，2表示-
            e = n // 3
            q = n % 3
            if n == 0:
                return '0'
            elif e == 0:
                return str(q)
            else:
                return ternary(e) + str(q)

        max_t = ternary(6560)  # 3的8次方
        sq = ternary(nn)
        l = len(max_t)
        if len(sq) < l:
            return '0' * (l - len(sq)) + sq
        else:
            return sq

    def vert(n):
        c_symbol = ten2ter(n)
        split_symbol = []
        for k in range(len(c_symbol)):
            if c_symbol[k] == '0':
                split_symbol.append('0')
            elif c_symbol[k] == '1':
                split_symbol.append('+')
            elif c_symbol[k] == '2':
                split_symbol.append('-')
        sq = []
        for i in range(len(c_symbol)):
            sq.extend(init_sq[i] + split_symbol[i])
        sq.extend(init_sq[8])
        return sq

    def del_all(L):
        LIS = []
        for i in range(len(L)):
            if L[i] != '0':
                LIS.append(L[i])
        return LIS

    def to_calculate(n):
        a = vert(n)
        index = []
        for i in range(len(a)):
            if a[i] == '+' or a[i] == '-':
                index.append(i)
        b = [a[0:index[0]]]
        for k in range(1, len(index)):
            b.append(a[index[k - 1]:index[k]])
        if index[-1] != 17:
            b.append(a[index[-1]:17])
        for i in range(len(b)):
            b[i] = del_all(b[i])

        return b

    def con_to_num(s):
        a = ''
        if s[0] == '+':
            l = len(s)
            for i in range(1, l):
                a = a + s[i]
            return int(a)
        if s[0] == '-':
            l = len(s)
            for i in range(1, l):
                a = a + s[i]
            return -1 * int(a)
        else:
            l = len(s)
            for i in range(0, l):
                a = a + s[i]
            return int(a)

    counting = 0
    for value_sum in range(1, 6561):
        b = to_calculate(value_sum)
        number = []
        for i in b:
            n = con_to_num(i)
            number.append(n)

        total = sum(number)
        if total == Max_values:
            print(number)
            counting = counting + 1

    return int(counting)


if __name__ == '__main__':
    print('Q1 Solution')
    Print_values()
    print('Q2 Solution')
    Matrix_multip()
    print('Q3 Solution')
    Pascal_triangle(100)
    Pascal_triangle(200)
    print('Q4 Solution')
    money = np.random.randint(1, 101)
    print(money)
    Least_moves(money)
    print('Q5 Solution')
    import matplotlib.pyplot as plt
    # the result have been shown
    s_n = [26, 11, 18, 8, 21, 12, 17, 8, 22, 12, 21, 11, 16, 15, 20, 8, 17, 11, 20, 15, 16, 11, 23, 18, 13,
           14, 21, 15, 19, 17, 14, 19, 19, 7, 14, 19, 19, 17, 18, 16, 17, 18, 10, 15, 26, 18, 15, 16, 12,
           17, 19, 9, 17, 21, 16, 13, 14, 16, 17, 17, 11, 13, 22, 14, 13, 15, 15, 15, 17, 7, 14, 17, 15, 12,
           13, 14, 14, 14, 10, 9, 19, 12, 13, 13, 12, 11, 12, 6, 12, 14, 16, 13, 11, 11, 10, 11, 7, 9, 17, 11]
    solution_number = []
    for i in range(1, 101):
        a = Find_expression(i)
        solution_number.append(a)
    Find_expression(100)
    i = list(range(1, 101))
    print('From 1 to 100, the amount of combination for each number')
    print(s_n)
    plt.plot(i, s_n)
    plt.show()
