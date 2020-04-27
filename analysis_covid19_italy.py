import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/dpc-covid19-ita-andamento-nazionale.csv')

print(df.info())

print(df.head())

correlation = df.corr()
plt.imshow(correlation)

print(correlation['deceduti'])

plt.figure()

df['totale_casi'].plot()
df['deceduti'].plot()
df['data'] = pd.to_datetime(df['data'])
first_day = df['data'].min()
interval = df['data']-first_day
plt.bar(interval.array.days, df['nuovi_attualmente_positivi'])
plt.xticks(interval.array.days, df['data'].array.date)
plt.tick_params(axis='x', labelrotation=45, left=True)
# plt.show()
plt.figure()
plt.scatter(df['nuovi_attualmente_positivi'][:-1].array,df['nuovi_attualmente_positivi'][1:].array)
plt.show()