import pandas as pd
import time

string = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())
print(string)
f = pd.read_csv("../individual_attribute.csv")

print(f.head())