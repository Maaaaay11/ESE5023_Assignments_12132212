# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:02:29 2021

@author: Maoma
"""

#WIND-OBSERVATION speed rate
#The rate of horizontal travel of air past a fixed point.
# MIN: 0000 MAX: 0900 UNITS: meters per second
# 9999 = Missing.

import pandas as pd
# read the csv file of wind 
wind = pd.read_csv("D:/python/ass2/2281305.csv")
# bulid a dataframe which split the 'WND' into five pieces
wind_speed = wind['WND'].str.split(',', expand = True)
# rename the head of columns
wind_speed.columns = ['dire_angle', 'dire_quality', 'type', 'speed_rate','speed_quality']
# delete the missing number
wind_speed = wind_speed[ ~ wind_speed['speed_rate'].str.contains('9999') ]
wind_speed['DATE'] = wind['DATE']
# turn the type of 'date' into datetime type
wind_speed['DATE'] = pd.to_datetime(wind_speed['DATE']) 
# use the dt function sort the data
wind_speed['Time'] = wind_speed['DATE'].dt.to_period('M')
# change the type of speed_rate
wind_speed['speed_rate'] = wind_speed['speed_rate'].apply(pd.to_numeric)
# build a dataframe,index is 'Time',value is the mean of 'speed_rate'
import numpy as np
pivot = pd.pivot_table(wind_speed, index=['Time'], values=['speed_rate'], aggfunc=np.mean)
# plot 
pivot.plot.line()