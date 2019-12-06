import time
start = time.time()

import pandas as pd
import numpy as np
from columns import * # Column Headers
from colspecs import * # Column length specs
from pprint import pprint
from io import StringIO
import os

from pandas.io import sql
from sqlalchemy import create_engine
# import pmysql

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="dev",
                               pw="rooting",
                               db="cdcnatality"))

# Read Files in 1Mb Chunks
file_path = "./data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt"
# file_path = "./Nat2018Head.txt" # Head File For Testing

infile = open(file_path, 'rb')

infile_size = os.path.getsize(file_path)
print("Total File Size Loaded (Bytes): ",infile_size)

# chunk_size=1024*64 #64kb
chunk_size=1024 * 10240 #1048576 bytes = 1024kb = 1Mb
chunks_number = infile_size//chunk_size # Integer division Result
print("Chunk Size: ",chunk_size," Total Number of Chunks is: ",chunks_number)

def read_in_chunks(infile, chunk_size=1024*64):
    count = 1
    while True:
        chunk = infile.read(chunk_size)
        if chunk:
            # pprint(chunk)
            # pprint(type(chunk))
            # yield chunk

            s=str(chunk,'utf-8')
            data = StringIO(s) 
            # df=pd.read_csv(data)

            df = pd.read_fwf(data, colspecs=list_colspecs, header=None,index=0 )
            df.columns = list_columns
            # print(df)
            # print(type(df))
            # df.to_csv('./csv/2018_final.csv', mode='a', header=False) # To CSV
            df.to_sql(con=engine, name='Nat2018us2', if_exists='append') # Code To Save Into Mysql/Mariadb Database

            print("Chunk # ",count,"/",chunks_number)
            count += 1
        else:
            # The chunk was empty, which means we're at the end
            # of the file
            return


read_in_chunks(infile, chunk_size) # Uncomment To Run Function

print("Done!")
print ('Execution Time: ', time.time()- start ,' Seconds')