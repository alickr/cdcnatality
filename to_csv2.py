import pandas as pd
import numpy as np
from columns import *
from colspecs import *

# colspecs = [(8,12),(12,14),(18,22),(22,23),(31,32),(32,33),(49,50),
#     (72,73),(73,74),(74,76),
#     (76,78),(78,79),(83,84),(103,104)
#     ]

# columns = ["DOB_YY", "DOB_MM", "DOB_TT","DOB_WK","BFACIL","F_FACILITY","BFACIL3",
#     "MAGE_IMPFLG","MAGE_REPFLG","MAGER",
#     "MAGER14","MAGER9","MBSTATE_REC","RESTATUS"
#     ]

df = pd.read_fwf('Nat2018Head copy.txt', colspecs=colspecs, header=None, )


# df1 = pd.DataFrame(df.values, columns = columns)
df_columns
df.columns = df_columns
df
# print(open('Nat2018Head.txt').read())
df_columns
colspecs


