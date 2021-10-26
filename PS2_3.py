# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:30:09 2021

@author: Maoma
"""
#ps3.1
import pandas as pd
flow_df = pd.read_csv("D:/python/ass2/load.csv")
#delete the NAN 
flow_df = flow_df.dropna()

#3.2
import numpy as np
flow_df['CDATE'] = pd.to_datetime(flow_df['CDATE']) 
flow_df['DATE'] = flow_df['CDATE'].dt.to_period('M')
pivot = pd.pivot_table(flow_df, index=['DATE'], values=['Flow'], aggfunc=np.mean)
# plot 
pivot.plot.line()

#3.3
# bulid a function which calculte these stastic number
def stats(x):
    return pd.Series([x.count(),x.min(),x.median(),x.mean(),x.max(),x.var()],
                     index = ['Count','Min','Median','Mean','Max','Var'])
stats(flow_df['Flow'])