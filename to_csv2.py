import pandas as pd
import numpy as np
from columns import * # Column Headers
from colspecs import * # Column length specs

df = pd.read_fwf('Nat2018Head.txt', colspecs=list_colspecs, header=None, )

df_columns
df.columns = list_columns
df