import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data_forPS2.csv')

df['date'] = df['Mon'].map(str) + '-' + df['Day'].map(str)
df_52602 = df[df['Station_Id_C'] == 52602]

df2 = df_52602.applymap(lambda x: 0 if x == 999999 else x)

cols_plot = ['PRS', 'TEM', 'RHU', 'VAP', 'PRE_1h']
axes = df2.plot(x='date', y=cols_plot, marker='.', linestyle='None', figsize=(11, 9), subplots=True)

axes[0].set_ylabel('PRS')
axes[1].set_ylabel('TEM')
axes[2].set_ylabel('RHU')
axes[3].set_ylabel('VAP')
axes[4].set_ylabel('PRE_1h')
plt.show()
