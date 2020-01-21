import numpy as np
import pandas as pd

df=pd.read_excel("Baseball INIT data.xlsx")
# ~ print(df[["BBB","BH"]])
print(np.array(df[["BR","BH","BBB","AVG","W","PH","PR"]]))
