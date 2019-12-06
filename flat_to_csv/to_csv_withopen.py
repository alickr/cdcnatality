import pandas as pd
import numpy as np
from columns import * # Column Headers
from colspecs import * # Column length specs
from pprint import pprint

file_path = "./Nat2018Head.txt"
# with open(file_path, 'rb') as f:
#     while True:
#         line = f.readline()
#         if line: 
#             print(line,"\n")

#             df = pd.read_fwf('Nat2018PublicUS.c20190509.r20190717.txt', colspecs=list_colspecs, header=None, )

#             df.columns = list_columns
#             df
#             type(df)

#             df.to_csv('./csv/Nat2018PublicUS.c20190509.r20190717.txt.csv', index = False)
#             print("Done")
#         else:
#             break
from io import StringIO

# Read Files in 1Mb Chunks
infile = open(file_path, 'rb')
def read_in_chunks(infile, chunk_size=1024*64):
    while True:
        chunk = infile.read(chunk_size)
        if chunk:
            # pprint(chunk)
            # pprint(type(chunk))
            # yield chunk

            s=str(chunk,'utf-8')

            data = StringIO(s) 

            # df=pd.read_csv(data)

            df = pd.read_fwf(data, colspecs=list_colspecs, header=None, )
            print(type(df))
            df.to_csv('./csv/test.csv', mode='a', header=False)


        else:
            # The chunk was empty, which means we're at the end
            # of the file
            return

# chunk_size=1024*64 #64kb
chunk_size=1024 * 1024 #1048576 bytes = 1024kb = 1Mb
chunk_size
# read_in_chunks(infile, chunk_size) # Uncomment To Run Test Function Call


# print("Done!")