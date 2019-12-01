
## AUTHOR :: innocent alfredo

import csv
import pandas as pd
import numpy as np
from matplotlib import style
from matplotlib import pyplot as plt
 
#Load dataset
chunksize = 2000000
for df_2016 in pd.read_csv('csv_folder/2016.csv', chunksize=chunksize):
    df_2016.append(df_2016)

   #head
    df_2016.head()

    #description
    df_2016.describe()

    #dataset shape
    df_2016.shape

    #dataset columns
    df_2016.columns
    #dataset info
    df_2016.info()

    #number of cigarate before pregnancy
Nbp = df_2016.groupby(['CIG_0'])
Nbp.first()

#count number of cigarate before pregnancy
Nbp.first().count()

#pre-pregnancy diabetes
prepd = df_2016.groupby(['RF_PDIAB'])
prepd.first()

prepd.first().count()

#pre-pregnancy hypertension
preht = df_2016.groupby(['RF_PHYPE'])
preht.first()
preht.first().count()
