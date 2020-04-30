import pandas as pd
from util import *

df_br = pd.read_csv('data/covid19_geral.csv', sep=';')

print(df_br.info())

print(df_br.head())

df_br['date'] = pd.to_datetime(df_br['data'], yearfirst=True, format='%Y-%m-%d')
estados = df_br['estado'].unique()
plt.figure(figsize=(16,9))
fmt = ['-o', '-.', '-^']
for i,estado in enumerate(np.sort(estados)):
    my_plot(df_br[df_br['estado'] == estado], 'casosAcumulados', fmt=fmt[int(i/9)],print_label=False)
plt.legend(np.sort(estados), ncol=3)
plt.title('Casos de COVID19 por estado')
plt.tick_params(axis='x', labelrotation=90, left=True)
plt.xticks(ticks=df_br['date'])
plt.savefig('figs/casos_brasil_por_estado.png')

casosNovos = []
casosAcumulados = []
obitosAcumulados = []
obitosNovos = []
for date in np.unique(df_br['date']):
    casosNovos.append(df_br[df_br['date'] == date]['casosNovos'].sum())
    casosAcumulados.append(df_br[df_br['date'] == date]['casosAcumulados'].sum())
    obitosNovos.append(df_br[df_br['date'] == date]['obitosNovos'].sum())
    obitosAcumulados.append(df_br[df_br['date'] == date]['obitosAcumulados'].sum())

plt.figure()
plt.bar(np.arange(len(df_br['date'].unique())), np.array(casosNovos))
plt.title('Novos casos de COVID19 no Brasil')
plt.savefig('figs/novos_casos_brasil.png')

plt.figure()
plt.plot_date(df_br['date'].unique(), np.array(casosAcumulados), xdate=True, fmt='-o')
plt.tick_params(axis='x', labelrotation=90, left=True)
plt.title('Casos acumulados de COVID19 no Brasil')
plt.xticks(ticks=df_br['date'])
plt.savefig('figs/casos_brasil.png')

plt.figure()
plt.bar(np.arange(len(df_br['date'].unique())), np.array(obitosNovos))
plt.title('Novos obitos de COVID19 no Brasil')
plt.savefig('figs/novos_obitos_brasil.png')

plt.figure()
plt.plot_date(df_br['date'].unique(), np.array(obitosAcumulados), xdate=True, fmt='-o')
plt.tick_params(axis='x', labelrotation=90, left=True)
plt.title('Obitos acumulados de COVID19 no Brasil')
plt.xticks(ticks=df_br['date'])
plt.savefig('figs/obitos_brasil.png')
