# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:50:23 2018

@author: gateway
"""

import numpy as np 
import pandas as pd 

itemsets = [["26"], ["51", "28", "27"], ["50"], ["8"], ["81", "15"], ["10"], ["81"]]
support = [0.06421, 0.00123, 0.04112, 0.0112, 0.12097, 0.08123, 0.0021334]
df = pd.DataFrame()
df["itemsets"]= itemsets
df["support"] = support

df.at[1,1] = 1.2
print(df)