# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:06:37 2021

@author: thoudd0701
"""

#4 add or double
def Least_moves(x):
    if x == 1:
        step = 0
    elif x >= 2:
        step = 0 
        for i in range (100):
            if x >= 2:
                #判断能否除以2，若余数为0继续除以2，并计数一次
                if x % 2 == 0:
                    x = x / 2
                    step += 1
                    continue
                #若除以2余数为1则减去1，并计数一次
                elif x % 2 == 1:
                    x = x - 1
                    step += 1
                    continue
                #若x<2，跳出循环
                else:
                    break
    print(step)
Least_moves(2)
Least_moves(5)
Least_moves(6)
