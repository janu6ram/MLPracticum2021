import os
import pandas as pd

path = "/home/ramgadde/Desktop/MLPracticum2021/input/combined_csv.csv"
data = pd.read_csv(path, error_bad_lines=False)

print(data.describe)