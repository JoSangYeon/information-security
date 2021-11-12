import pandas as pd
import numpy as np

ind_att = pd.read_csv('..\individual_attribute.csv')

query = ((ind_att["g_id"] == "KMU") & (ind_att["u_id"] == "JSY17"))
print(np.all(query == False))
# print(ind_att[query])
