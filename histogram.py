import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import statistics as stat
df = pd.read_csv(r"C:/ajnas.out/btech/ML PROJECTS/lois_continuous.csv")
print(df.head())
df_new =df[df['ID']=='S1']
t = df_new['Temperature water continuous']
o = df_new['Oxygen dissolved continuous']
print(t.dtypes)
print(o.dtypes)
print("Mean of Temperature of water continous : ",stat.mean(t))
print("Median of Oxygen dissolved continous : ",stat.median(o))
x = np.array(t)
t.hist()
plt.title('louis continous')
plt.xlabel('Distribution of temperation')
plt.ylabel('Time period of study')
plt.show()