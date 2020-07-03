 ### *************
 ### THE INITIATOR
 ### *************

import warnings
warnings.filterwarnings("ignore")

import numpy as np 
import pandas as pd
pd.set_option('display.max_columns', 999)
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_colwidth', -1)

import seaborn as sns
sns.set_style('whitegrid')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
%matplotlib inline


## THE LAST TOUCH
print('** TITLE OF THE PROJECT **')
print("-"*25)

import gc
import os
for x in os.listdir("input/"):
    print(x)
print("-"*25)

### DATER
### This part is optional, no need to run unless required

# import sys
# import time
# from datetime import datetime, timedelta

# bgn      = str(datetime.today().strftime('%Y%m%d'))
# snp         = str(str((datetime.today() - timedelta(1)).strftime('%Y%m%d')))[0:6] + '01'
# aybasi      = str(datetime.today().replace(day=1).strftime('%Y%m%d'))
# gecenay_son = str((datetime.today().replace(day=1) - timedelta(1)).strftime('%Y%m%d'))
# gecenay_ilk = str((datetime.today().replace(day=1) - timedelta(1)).strftime('%Y%m%d'))[0:6] + '01'

print ("Initiation is DONE !!")
print("-"*25)