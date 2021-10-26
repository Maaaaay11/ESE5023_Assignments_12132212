# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:18:07 2021

@author: Maoma
"""
##PS1.1
import pandas as pd
#read the csv file
eqs_df = pd.read_csv("D:/python/ass2/Sig_Eqs.csv")
#group by the 'Country' and sum the deaths and sort in descending order
eqs_total_death = eqs_df.groupby(['Country']).sum().sort_values('Deaths', ascending=False)
#print the top 10 term
print(eqs_total_death['Deaths'].head(10))

#####PS1.2
import matplotlib.pyplot as plt
#choose that  magnitude > 6 
mag = eqs_df.loc[eqs_df['Mag']> 6.0 ]
#group by the year, and count the  magnitude>6,then plot
mag = mag.groupby(['Year']).count()['Mag'].plot()
plt.show()


###PS1.3
def CountEq_LargestEq(x):
# bulid a dataframe which contains input country
    country = eqs_df.loc[eqs_df['Country'] == x]
# use the new dataframe count the 'year' to calculate the total number of earthquakes
    country_sum = country.count()['Year']
# use the idxmax function to get the index of the max number of country, and get the value of year/month/day
    Y = int(eqs_df['Year'].iloc[country['Mag'].idxmax()])
    M = int(eqs_df['Mo'].iloc[country['Mag'].idxmax()])
    D = int(eqs_df['Dy'].iloc[country['Mag'].idxmax()])
# output the date of max magnitude
    print(x,country_sum ,str(Y) +"-"+ str(M) + "-"+ str(D))

CountEq_LargestEq('JAPAN')
