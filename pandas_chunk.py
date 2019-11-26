import time
start = time.time()

import pandas as pd
import numpy as np
from columns import * # Column Headers
from colspecs import * # Column length specs
from pprint import pprint
from io import StringIO
import os

file_path = "./data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt"

df_chunk = pd.read_fwf(r'./data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt', chunksize=1000000,colspecs=list_colspecs, header=None )

# Each chunk is in df format
for chunk in df_chunk:
    
    chunk.to_csv('./csv/2018_final3_chunk.csv', mode='a', header=False, index=False)
    # print("Chunk # ",count,"/",chunks_number)
    # count += 1

print("Done!")
print ('Execution Time: ', time.time()- start ,' Seconds')