import pandas as pd
import numpy as np
from columns import * # Column Headers
from colspecs import * # Column length specs

df = pd.read_fwf('Nat2018PublicUS.c20190509.r20190717.txt', colspecs=list_colspecs, header=None, )

df.columns = list_columns
df
type(df)

# ----------------------------- Create File to Submit --------------------------------
# df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
# ...                    'mask': ['red', 'purple'],
# ...                    'weapon': ['sai', 'bo staff']})
# df.to_csv(index=False)
df.to_csv('./csv/Nat2018PublicUS.c20190509.r20190717.txt.csv', index = False)
print("Done")
