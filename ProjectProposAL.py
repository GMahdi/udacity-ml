# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 07:06:08 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
agricultre_df = pd.read_csv('API_AG.LND.AGRI.ZS_DS2_en_csv_v2.csv', index_col= 1,low_memory=False, skipinitialspace=True, header=2)
literacy_df = pd.read_csv('API_SE.ADT.LITR.ZS_DS2_en_csv_v2.csv', index_col= 1, low_memory=False, skipinitialspace=True, header=2)

#agricultre_df = agricultre_df.dropna()
#literacy_df = literacy_df.dropna()
#literacy_df = literacy_df.rename(columns = [literacy_df.columns[i] = 'Agri: ' + literacy_df.columns[i] for i in range(3, len(literacy_df.columns))])
new_names = ['Agri: '+i for i in agricultre_df.columns ]
agricultre_df.rename(columns=dict(zip(agricultre_df.columns, new_names)), inplace=True)

new_names = ['Literacy: '+i for i in literacy_df.columns ]
literacy_df.rename(columns=dict(zip(literacy_df.columns, new_names)), inplace=True)


#print(literacy_df.columns)

    
agri_liter_df = agricultre_df.join(literacy_df,how='inner')
#agri_liter_us = agri_liter_df[agri_liter_df['Country Code']=='USA']
#print(
#agri_liter_df['Agri: 2015'].fillna(0)
#agri_liter_df['Literacy: 2014'].fillna(0)
plt.scatter(agri_liter_df['Agri: 2014'], agri_liter_df['Literacy: 2014'])
#plt.scatter(agri_liter_us)
#plt.plot(agri_liter_df['Agri: 2014'])
agri_liter_df['Agri: 2014'].plot(grid=True, figsize=(10,5))
plt.show()
#print(literacy_df.head())
#print(agricultre_df.head())
#print(agri_liter_df.columns)
#print(agri_liter_df['Agri: 2015'].head())
#agri_liter_df['Agri: 2015'].replace(np.NaN,0)
#print(agri_liter_df['Literacy: 2014'].tail())

#plt.plot(agri_liter_df['Agri: 2015'])
#plt.show()
