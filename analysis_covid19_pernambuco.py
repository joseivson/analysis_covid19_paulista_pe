import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from util import *

df_br = pd.read_csv('data/covid19-' + 'brasil' + '.csv')
df_br['date'] = pd.to_datetime(df_br['date'], yearfirst=True, format='%Y-%m-%d')
df_paulista = pd.read_csv('data/covid19-paulista.csv')
df_paulista['date'] = pd.to_datetime(df_paulista['date'], yearfirst=True, format='%Y-%m-%d')
df_recife = pd.read_csv('data/covid19-recife.csv')
df_recife['date'] = pd.to_datetime(df_recife['date'], yearfirst=True, format='%Y-%m-%d')
df_pe = pd.read_csv('data/covid19-pernambuco.csv')
df_pe['date'] = pd.to_datetime(df_pe['date'], yearfirst=True, format='%Y-%m-%d')

compare_places(df_br[df_br['state'] == 'SP'],
                df_br[df_br['state'] == 'PE'],
                'confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                'SÃO PAULO',
                'PERNAMBUCO')

compare_places(df_br[df_br['state'] == 'SP'],
                df_br[df_br['state'] == 'PE'],
                'death_rate',
                'Taxa de mortalidade',
                'SÃO PAULO',
                'PERNAMBUCO')

compare_places(df_br[df_br['state'] == 'CE'],
                df_br[df_br['state'] == 'PE'],
                'confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                'CEARÁ',
                'PERNAMBUCO')

compare_places(df_br[df_br['state'] == 'CE'],
                df_br[df_br['state'] == 'PE'],
                'death_rate',
                'Taxa de mortalidade',
                'CEARÁ',
                'PERNAMBUCO')

compare_places(df_recife,
                df_paulista,
                'confirmed_per_100k_inhabitants',
                'Confirmados por 100 mil habitantes',
                'RECIFE',
                'PAULISTA')

compare_places(df_recife,
                df_paulista,
                'death_rate',
                'Taxa de mortalidade',
                'RECIFE',
                'PAULISTA')

df_places = [df_pe, df_paulista, df_recife]
places = ['pernambuco', 'paulista', 'recife']

for i,df_place in enumerate(df_places):
    plt.figure(figsize=(16,9))
    my_bar(df_place, 'confirmed')
    plt.legend(['Novos casos confirmados em ' + str.upper(places[i])])
    plt.title('Novos casos diários de COVID19')
    plt.savefig('figs/novos_casos_' + places[i] + '.png')

    plt.figure(figsize=(16,9))
    my_plot(df_place, 'confirmed')
    my_plot(df_place, 'deaths', fmt='-+')
    plt.legend(['Confirmados em ' + str.upper(places[i]), 'Mortes em ' + str.upper(places[i])])
    plt.title('Casos de COVID19')
    plt.savefig('figs/casos_' + str(places[i]) + '.png')

    plt.figure(figsize=(16,9))
    my_plot(df_place, 'confirmed_per_100k_inhabitants')
    plt.legend(['Confirmados por 100 mil habitantes em ' + str.upper(places[i])])
    plt.title('Casos por 100 mil de COVID19')
    plt.savefig('figs/casos_100k_' + str(places[i]) + '.png')
    
    plt.figure(figsize=(16,9))
    my_plot(df_place, 'death_rate', '-+')
    plt.legend(['Taxa de mortalidade em ' + str.upper(places[i])])
    plt.title('Mortalidade da COVID19')
    plt.savefig('figs/mortalidade_' + str(places[i]) + '.png')
