import time
start = time.time()
import os

from pandas.io import sql
from sqlalchemy import create_engine
# import pmysql

from io import StringIO
import pandas as pd
import numpy as np
from columns import * # Column Headers
from colspecs import * # Column length specs
from pprint import pprint

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="dev",
                               pw="rooting",
                               db="cdcnatality"))


# df.to_sql(con=engine, name='table_name', if_exists='replace')


# Read Files in 1Mb Chunks
# file_path = "./data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt" #Actual File
file_path = "./Nat2018Head.txt" # Head File For Testing

infile = open(file_path, 'rb')

infile_size = os.path.getsize(file_path)
print("Total File Size Loaded (Bytes): ",infile_size)

chunk_size=1024*64 #64kb
# chunk_size=1024 * 1024 #1048576 bytes = 1024kb = 1Mb
chunks_number = infile_size//chunk_size # Integer division Result
print("Chunk Size: ",chunk_size," Total Number of Chunks is: ",chunks_number)

df = pd.read_fwf(file_path, colspecs=list_colspecs, header=None, )
df.columns = list_columns
# df = pd.read_fwf(infile, colspecs=list_colspecs, header=None, )
df.to_sql(con=engine, name='table2', if_exists='replace') # Code To Save Into Mysql/Mariadb Database


read_in_chunks(infile, chunk_size) # Uncomment To Run Function

print("Done!")
print ('Execution Time: ', time.time()- start ,' Seconds')