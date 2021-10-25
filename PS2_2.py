import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./2281305.csv', header=0, encoding='utf-8')
wind_df = df[['DATE', 'WND']]
wind_df['wind_speed'] = wind_df['WND'].map(lambda x: x.split(',')[3])
wind_df['month'] = wind_df['DATE'].map(lambda x: x[0:7])
wind_df['wind_speed'] = wind_df['wind_speed'].map(lambda x: float(x))
A = wind_df.groupby('month').mean()
A['wind_speed'].plot()
plt.show()
