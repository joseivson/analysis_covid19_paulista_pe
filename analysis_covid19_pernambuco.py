import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from util import *
from projection import *

df_br = pd.read_csv('data/covid19-' + 'brasil' + '.csv')
df_br['date'] = pd.to_datetime(df_br['date'], yearfirst=True, format='%Y-%m-%d')
df_paulista = pd.read_csv('data/covid19-paulista.csv')
df_paulista['date'] = pd.to_datetime(df_paulista['date'], yearfirst=True, format='%Y-%m-%d')
df_recife = pd.read_csv('data/covid19-recife.csv')
df_recife['date'] = pd.to_datetime(df_recife['date'], yearfirst=True, format='%Y-%m-%d')
df_pe = pd.read_csv('data/covid19-pernambuco.csv')
df_pe['date'] = pd.to_datetime(df_pe['date'], yearfirst=True, format='%Y-%m-%d')
df_pe_city = pd.read_csv('data/covid19-pernambuco_per_city.csv')
df_pe_city['date'] = pd.to_datetime(df_pe_city['date'], yearfirst=True, format='%Y-%m-%d')

df_sp = df_br[df_br['state'] == 'SP']

compare_places([df_br[df_br['state'] == 'SP'],
                df_br[df_br['state'] == 'PE']],
                'last_available_confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                ['SÃO PAULO','PERNAMBUCO'])

compare_places([df_br[df_br['state'] == 'SP'],
                df_br[df_br['state'] == 'PE']],
                'last_available_death_rate',
                'Taxa de mortalidade',
                ['SÃO PAULO','PERNAMBUCO'])

compare_places([df_br[df_br['state'] == 'CE'],
                df_br[df_br['state'] == 'PE']],
                'last_available_confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                ['CEARÁ','PERNAMBUCO'])

compare_places([df_br[df_br['state'] == 'CE'],
                df_br[df_br['state'] == 'PE']],
                'last_available_death_rate',
                'Taxa de mortalidade',
                ['CEARÁ','PERNAMBUCO'])

compare_places([df_br[df_br['state'] == 'PB'],
                df_br[df_br['state'] == 'PE']],
                'last_available_confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                ['PARAÍBA','PERNAMBUCO'])

compare_places([df_br[df_br['state'] == 'PB'],
                df_br[df_br['state'] == 'PE']],
                'last_available_death_rate',
                'Taxa de mortalidade',
                ['PARAÍBA','PERNAMBUCO'])

compare_places([df_recife,df_paulista],
                'last_available_confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                ['RECIFE','PAULISTA'])

compare_places([df_recife,df_paulista],
                'last_available_death_rate',
                'Taxa de mortalidade',
                ['RECIFE','PAULISTA'])

compare_places([df_br[df_br['state'] == 'SP'],
                df_br[df_br['state'] == 'PE'],
                df_br[df_br['state'] == 'CE'],
                df_br[df_br['state'] == 'PB']],
                'last_available_confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                ['SÃO PAULO','PERNAMBUCO', 'CEARÁ', 'PARAÍBA'])

df_places = [df_pe, df_paulista, df_recife, df_sp]
places = ['pernambuco', 'paulista', 'recife', 'são paulo']

for i,df_place in enumerate(df_places):
    my_bar(df_place, 'new_confirmed', 
            ['Novos casos confirmados em ' + str.upper(places[i])],
            'Novos casos diários de COVID19',
            'figs/novos_casos_' + places[i] + '.png')

    my_bar(df_place, 'new_deaths', 
            ['Novos óbitos em ' + str.upper(places[i])],
            'Novos óbitos diários de COVID19',
            'figs/novos_obitos_' + places[i] + '.png')

    plt.figure(figsize=(16,9))
    my_plot(df_place, 'last_available_confirmed')
    my_plot(df_place, 'last_available_deaths', fmt='-+')
    plt.legend(['Confirmados em ' + str.upper(places[i]), 'Mortes em ' + str.upper(places[i])])
    plt.title('Casos de COVID19')
    plt.savefig('figs/casos_' + str(places[i]) + '.png')
    plt.close()

    plt.figure(figsize=(16,9))
    my_plot(df_place, 'last_available_confirmed_per_100k_inhabitants')
    plt.legend(['Confirmados por 100 mil habitantes em ' + str.upper(places[i])])
    plt.title('Casos por 100 mil de COVID19')
    plt.savefig('figs/casos_100k_' + str(places[i]) + '.png')
    plt.close()

    plt.figure(figsize=(16,9))
    my_plot(df_place, 'last_available_death_rate', '-+')
    plt.legend(['Taxa de mortalidade em ' + str.upper(places[i])])
    plt.title('Mortalidade da COVID19')
    plt.savefig('figs/mortalidade_' + str(places[i]) + '.png')
    plt.close()

    plt.figure(figsize=(16,9))
    legend = []
    for day in [3,7,14]:
        plt.plot_date(df_place.iloc[:-day]['date'], mean_mobile(df_place['new_confirmed'].array, day), fmt='-')
        legend.append('Últimos ' + str(day) + ' dias em ' + str(places[i]))
    plt.legend(legend)
    plt.title('Média de novos casos nos últimos dias')
    plt.savefig('figs/media_movel_' + str(places[i]) + '.png')
    plt.close()

plt.figure(figsize=(16,9))
df_br.sort_values(by='last_available_death_rate', ascending=False, inplace=True)
last = df_br['is_last']
plt.bar(df_br[last]['state'], df_br[last]['last_available_death_rate'].apply(percentage))
plt.ylabel('Em porcentagem (%)')
plt.title('Taxa de mortalidade por COVID19 nos estados')
plt.savefig('figs/taxa_mortalidade_estados_brasil.png')
plt.close()

insert_division_column(df_br, 'death_per_100k', 'last_available_deaths', 'estimated_population_2019')
df_br['death_per_100k'] = df_br['death_per_100k'].apply(per_100k)
df_br.sort_values(by='death_per_100k', ascending=False, inplace=True)
last = df_br['is_last']
plt.figure(figsize=(16,9))
plt.bar(df_br[last]['state'], df_br[last]['death_per_100k'])
plt.title('Mortos por COVID19 a cada 100 mil habitantes nos estados')
plt.savefig('figs/mortalidade_100k_estados_brasil.png')
plt.close()

plt.figure(figsize=(16,9))
plt.scatter(df_br[last]['death_per_100k'], 
            df_br[last]['last_available_confirmed_per_100k_inhabitants'])
for state in df_br[last]['state']:
    plt.text(df_br[last & (df_br['state']==state)]['death_per_100k'], 
            df_br[last & (df_br['state']==state)]['last_available_confirmed_per_100k_inhabitants'],
            state)
    if state == 'SP':
        plt.scatter(df_br[last & (df_br['state'] == 'SP')]['death_per_100k'], 
            df_br[last & (df_br['state'] == 'SP')]['last_available_confirmed_per_100k_inhabitants'],
            c='r')
plt.title('Casos e Mortes por COVID19')
plt.xlabel('Mortes a cada 100 mil habitantes')
plt.ylabel('Casos a cada 100 mil habitantes')
plt.savefig('figs/confirmed_x_death_per_100k_estados.png')
plt.close()

last = df_pe_city['is_last']
insert_division_column(df_pe_city, 'death_per_100k', 'last_available_deaths', 'estimated_population_2019')
df_pe_city['death_per_100k'] = df_pe_city['death_per_100k'].apply(per_100k)
plt.figure(figsize=(16,9))
plt.scatter(df_pe_city[last]['death_per_100k'], 
            df_pe_city[last]['last_available_confirmed_per_100k_inhabitants'])
for city in df_pe_city[last]['city']:
    if (df_pe_city[last & (df_pe_city['city']==city)]['death_per_100k'] > 0).bool():
        plt.text(df_pe_city[last & (df_pe_city['city']==city)]['death_per_100k'], 
                df_pe_city[last & (df_pe_city['city']==city)]['last_available_confirmed_per_100k_inhabitants'],
                city)
plt.title('Casos e Mortes por COVID19')
plt.xlabel('Mortes a cada 100 mil habitantes')
plt.ylabel('Casos a cada 100 mil habitantes')
plt.savefig('figs/confirmed_x_death_per_100k_cidades.png')
plt.close()

from matplotlib.cm import ScalarMappable
sm = ScalarMappable()
sm.set_clim(0,26)

fig,ax = plt.subplots()
df_br.sort_values(by='last_available_confirmed', ascending=True, inplace=True)
for date in df_br['date'].unique():
    
    previous_sum = 0
    for i,state in enumerate(df_br[df_br['date'] == date]['state']):
        current_state = df_br[(df_br['date'] == date) & (df_br['state'] == state)]
        if i == 0:
            ax.bar(date, current_state['last_available_confirmed'], label=state, color=sm.to_rgba([i]))
        else:
            ax.bar(date, current_state['last_available_confirmed'], label=state, bottom=previous_sum, color=sm.to_rgba([i]))

        previous_sum += current_state['last_available_confirmed'].array

plt.savefig('figs/acumulado_casos.png')
plt.close()
