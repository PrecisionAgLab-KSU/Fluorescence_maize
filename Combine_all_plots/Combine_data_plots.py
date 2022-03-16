# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Dr. Dipankar Mandal, dmandal@ksu.edu

"""
# ----------------------------------------------------------------------------
  # Copyright (C) 2022 by PrecisionAG, Agronomy, KSU
 
  # This program is free software; you can redistribute it and/or modify it
  # under the terms of the GNU General Public License as published by the Free
  # Software Foundation; either version 3 of the License, or (at your option)
  # any later version.
  # This program is distributed in the hope that it will be useful, but WITHOUT
  # ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
  # FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
  # more details.
 
  # You should have received a copy of the GNU General Public License along
  # with this program; if not, see http://www.gnu.org/licenses/
# -----------------------------------------------------------------------------



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [12,2]
import matplotlib.dates as mdates
import matplotlib.pyplot as plt



filename = 'ardec0710'
filename2 = 'ardec0710'
s = 'sumindex'
## Reading Low management zone----------------------------------------------------------------
df1 = pd.read_excel(filename+'_Plot1'+'_WTdenoised_'+s+'.xlsx')
df20 = pd.read_excel(filename+'_Plot20'+'_WTdenoised_'+s+'.xlsx')
df37 = pd.read_excel(filename+'_Plot37'+'_WTdenoised_'+s+'.xlsx')
df58 = pd.read_excel(filename2+'_Plot58'+'_WTdenoised_'+s+'.xlsx')
df60 = pd.read_excel(filename2+'_Plot60'+'_WTdenoised_'+s+'.xlsx')
df16 = pd.read_excel(filename+'_Plot16'+'_WTdenoised_'+s+'.xlsx')
df19 = pd.read_excel(filename+'_Plot19'+'_WTdenoised_'+s+'.xlsx')
df41 = pd.read_excel(filename+'_Plot41'+'_WTdenoised_'+s+'.xlsx')
df42 = pd.read_excel(filename+'_Plot42'+'_WTdenoised_'+s+'.xlsx')
df17 = pd.read_excel(filename+'_Plot17'+'_WTdenoised_'+s+'.xlsx')
df21 = pd.read_excel(filename+'_Plot21'+'_WTdenoised_'+s+'.xlsx')
df35 = pd.read_excel(filename+'_Plot35'+'_WTdenoised_'+s+'.xlsx')
df36 = pd.read_excel(filename+'_Plot36'+'_WTdenoised_'+s+'.xlsx')
df15 = pd.read_excel(filename+'_Plot15'+'_WTdenoised_'+s+'.xlsx')
df18 = pd.read_excel(filename+'_Plot18'+'_WTdenoised_'+s+'.xlsx')
df57 = pd.read_excel(filename2+'_Plot57'+'_WTdenoised_'+s+'.xlsx')
df59 = pd.read_excel(filename2+'_Plot59'+'_WTdenoised_'+s+'.xlsx')
df38 = pd.read_excel(filename+'_Plot38'+'_WTdenoised_'+s+'.xlsx')
df39 = pd.read_excel(filename+'_Plot39'+'_WTdenoised_'+s+'.xlsx')
df40 = pd.read_excel(filename+'_Plot40'+'_WTdenoised_'+s+'.xlsx')
df43 = pd.read_excel(filename+'_Plot43'+'_WTdenoised_'+s+'.xlsx')

## Reading medium management zone----------------------------------------------------------------
df3 = pd.read_excel(filename+'_Plot3'+'_WTdenoised_'+s+'.xlsx')
df12 = pd.read_excel(filename+'_Plot12'+'_WTdenoised_'+s+'.xlsx')
df32 = pd.read_excel(filename+'_Plot32'+'_WTdenoised_'+s+'.xlsx')
df23 = pd.read_excel(filename+'_Plot23'+'_WTdenoised_'+s+'.xlsx')
df24 = pd.read_excel(filename+'_Plot24'+'_WTdenoised_'+s+'.xlsx')
df46 = pd.read_excel(filename+'_Plot46'+'_WTdenoised_'+s+'.xlsx')
df56 = pd.read_excel(filename2+'_Plot56'+'_WTdenoised_'+s+'.xlsx')
df2 = pd.read_excel(filename+'_Plot2'+'_WTdenoised_'+s+'.xlsx')
df5 = pd.read_excel(filename+'_Plot5'+'_WTdenoised_'+s+'.xlsx')
df45 = pd.read_excel(filename+'_Plot45'+'_WTdenoised_'+s+'.xlsx')
df55 = pd.read_excel(filename2+'_Plot55'+'_WTdenoised_'+s+'.xlsx')
df4 = pd.read_excel(filename+'_Plot4'+'_WTdenoised_'+s+'.xlsx')
df14 = pd.read_excel(filename+'_Plot14'+'_WTdenoised_'+s+'.xlsx')
df34 = pd.read_excel(filename+'_Plot34'+'_WTdenoised_'+s+'.xlsx')
df54 = pd.read_excel(filename2+'_Plot54'+'_WTdenoised_'+s+'.xlsx')
df13 = pd.read_excel(filename+'_Plot13'+'_WTdenoised_'+s+'.xlsx')
df22= pd.read_excel(filename+'_Plot22'+'_WTdenoised_'+s+'.xlsx')
df33 = pd.read_excel(filename+'_Plot33'+'_WTdenoised_'+s+'.xlsx')
df44 = pd.read_excel(filename+'_Plot44'+'_WTdenoised_'+s+'.xlsx')

## Reading High management zone----------------------------------------------------------------
df11 = pd.read_excel(filename+'_Plot11'+'_WTdenoised_'+s+'.xlsx')
df26 = pd.read_excel(filename+'_Plot26'+'_WTdenoised_'+s+'.xlsx')
df29 = pd.read_excel(filename+'_Plot29'+'_WTdenoised_'+s+'.xlsx')
df52 = pd.read_excel(filename2+'_Plot52'+'_WTdenoised_'+s+'.xlsx')
df8 = pd.read_excel(filename+'_Plot8'+'_WTdenoised_'+s+'.xlsx')
df28 = pd.read_excel(filename+'_Plot28'+'_WTdenoised_'+s+'.xlsx')
df31 = pd.read_excel(filename+'_Plot31'+'_WTdenoised_'+s+'.xlsx')
df51 = pd.read_excel(filename2+'_Plot51'+'_WTdenoised_'+s+'.xlsx')
df7 = pd.read_excel(filename+'_Plot7'+'_WTdenoised_'+s+'.xlsx')
df25 = pd.read_excel(filename+'_Plot25'+'_WTdenoised_'+s+'.xlsx')
df47 = pd.read_excel(filename+'_Plot47'+'_WTdenoised_'+s+'.xlsx')
df50 = pd.read_excel(filename+'_Plot50'+'_WTdenoised_'+s+'.xlsx')
df10 = pd.read_excel(filename+'_Plot10'+'_WTdenoised_'+s+'.xlsx')
df27 = pd.read_excel(filename+'_Plot27'+'_WTdenoised_'+s+'.xlsx')
df48 = pd.read_excel(filename+'_Plot48'+'_WTdenoised_'+s+'.xlsx')
df49 = pd.read_excel(filename+'_Plot49'+'_WTdenoised_'+s+'.xlsx')
df6 = pd.read_excel(filename+'_Plot6'+'_WTdenoised_'+s+'.xlsx')
df9 = pd.read_excel(filename+'_Plot9'+'_WTdenoised_'+s+'.xlsx')
df30 = pd.read_excel(filename+'_Plot30'+'_WTdenoised_'+s+'.xlsx')
df53 = pd.read_excel(filename2+'_Plot53'+'_WTdenoised_'+s+'.xlsx')



framef = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,
          df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,
          df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,
          df31,df32,df33,df34,df35,df36,df37,df38,df39,df40,
          df41,df42,df43,df44,df45,df46,df47,df48,df49,df50,
          df51,df52,df53,df54,df55,df56,df57,df58,df59,df60]
dfoo = pd.concat(framef)

# remove rows by filtering
df0 = dfoo[dfoo['Unnamed: 0'] == 'Values']
del df0['Unnamed: 0']

df0.columns =['NBI_R', 'NBI_G', 'NBI_B', 'NBI1', 'CHL', 'CHL1', 'FLAV','NBI_R_std', 'NBI_G_std', 'NBI_B_std', 'NBI1_std', 'CHL_std', 'CHL1_std', 'FLAV_std']


df0.reset_index(inplace=True, drop=True) 


