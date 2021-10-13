# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:02:37 2021

@author: thoudd0701
"""
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b<c:
            print(c,b,a)
            
Print_values(4,13,9)
Print_values(4,2,9)