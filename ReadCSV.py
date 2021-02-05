import os
import pandas as pd

directory = os.path.join("c:\\","")
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           f=open(file, 'r')
           #  perform calculation
           pd.read_csv(f)
           f.close()

