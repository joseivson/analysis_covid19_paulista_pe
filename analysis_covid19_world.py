import pandas as pd
import matplotlib.pyplot as plt
from util import *
import os

df_world = pd.read_csv('data/owid-covid-data.csv')
df_world['date'] = pd.to_datetime(df_world['date'], yearfirst=True, format='%Y-%m-%d')

df_br = pd.read_csv('data/covid19-' + 'brasil' + '.csv')
df_br['date'] = pd.to_datetime(df_br['date'], yearfirst=True, format='%Y-%m-%d')
df_sp = df_br[df_br['state'] == 'SP']
def times10(x):
    return x*10

df_sp['total_cases_per_million'] = df_sp['last_available_confirmed_per_100k_inhabitants'].apply(times10)

if not os.path.isdir('figs/world'):
    os.mkdir('figs/world')

def plot_from_first_day(df, countries, column, location):
    for country in countries:
        after_first_case = (df[location]==country) & (df[column]>0)
        dates = df[after_first_case]['date']
        plt.plot(dates-dates.min(), df[after_first_case][column])

plt.figure(figsize=(16,9))
countries = ['Italy', 'United States', 'Brazil', 'China', 'Spain', 'São Paulo']
for country in countries[:-1]:
    my_plot(df_world[df_world['location']==country], 'total_cases', grid=False, date_int=7, fmt='-')
my_plot(df_sp, 'last_available_confirmed', grid=False, fmt='--', date_int=7)
plt.legend(countries)
plt.title('Total de casos por país')
plt.savefig('figs/world/total_cases.png')
plt.close()

plt.figure(figsize=(16,9))
plot_from_first_day(df_world, ['Italy', 'United States', 'Brazil', 'China', 'Spain'], 'total_cases', 'location')
plot_from_first_day(df_sp, ['SP'], 'last_available_confirmed', 'state')
plt.legend(['Itália', 'Estados Unidos', 'Brasil', 'China', 'Espanha', 'São Paulo'])
plt.title('Total de casos por país após o 1º caso')
plt.savefig('figs/world/total_cases_after_first.png')
plt.close()

plt.figure(figsize=(16,9))
countries = ['Italy', 'United States', 'Brazil', 'China', 'Spain', 'São Paulo']
for country in countries[:-1]:
    my_plot(df_world[df_world['location']==country], 'total_cases_per_million', grid=False, date_int=7, fmt='-')
my_plot(df_sp, 'total_cases_per_million', grid=False, date_int=7, fmt='--')
plt.legend(countries)
plt.title('Total de casos por 1M por país')
plt.savefig('figs/world/total_cases_1M.png')
plt.close()

plt.figure(figsize=(16,9))
plot_from_first_day(df_world, ['Italy', 'United States', 'Brazil', 'China', 'Spain'], 'total_cases_per_million', 'location')
plot_from_first_day(df_sp, ['SP'], 'total_cases_per_million', 'state')
plt.legend(['Itália', 'Estados Unidos', 'Brasil', 'China', 'Espanha', 'São Paulo'])
plt.title('Total de casos por país após o 1º caso por 1M')
plt.savefig('figs/world/total_cases_1M_after_first.png')
plt.close()