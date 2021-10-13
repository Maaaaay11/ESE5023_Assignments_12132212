# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:06:24 2021

@author: thoudd0701
"""

#3.pascal triangle
def Pascal_triangle(k):
        result = []
        for i in range(k):
            result.append([1]*(i+1))
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        #函数返回第K行的值
        return result[k-1]
print(Pascal_triangle(50))
print(Pascal_triangle(100))