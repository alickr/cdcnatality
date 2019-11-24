import time
start = time.time()

import pandas as pd
import numpy as np
from columns import * # Column Headers
from colspecs import * # Column length specs
from io import StringIO

file_path = "./data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt"
# file_path = "./Nat2018Head.txt"
fh = open(file_path)
count=1
# line = fh.readline()
# type(line)
# # s=str(line,'utf-8')
# data = StringIO(line)
# data
# df = pd.read_fwf(data, colspecs=list_colspecs, header=None, )
# df
# exit()
for line in fh:
    # in python 2
    # print line
    # in python 3

    data = StringIO(line)
    # # df=pd.read_csv(data)
    # print(type(line))
    df = pd.read_fwf(data, colspecs=list_colspecs, header=None, )
    # print(type(df))
    df.to_csv('./csv/2018_briths.csv', mode='a', header=False, index=False)
    print("Line # ",count)
    count += 1

    # print(line)
fh.close()

print("Done!")
print ('Execution Time: ', time.time()- start ,' Seconds')