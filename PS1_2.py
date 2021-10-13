# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:06:07 2021

@author: thoudd0701
"""

#2.1 creat two matrix
import numpy as np
# 生成5*10的矩阵
M1 = np.random.randint(0,50,size=(5,10))
print( M1 )
# 生成10*5的矩阵
M2 = np.random.randint(0,50,size=(10,5))
print( M2 )

#2.2 A function of matrix multiplication                                                          
def Matrix_multip(A, B):
# 获取矩阵的行列个数
    row_A = A.shape[0]
    col_A = A.shape[1]
    row_B = B.shape[0]
    col_B = B.shape[1]
# 判断两矩阵能否做乘法
    if col_A == row_B:
# 建立一个0数组
        result =[[0 for i in range(row_A)] for j in range(col_B)] 
        for i in range(0,row_A):
            for j in range(0,col_B):
                for k in range(0,row_B):
                    result[i][j] += A[i][k] * B[k][j]
        return result
result = Matrix_multip(M1, M2)
print(result)

print(np.dot(M1,M2))