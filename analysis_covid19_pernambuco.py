import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from util import *

places = ['pernambuco', 'paulista', 'recife']
legend = []

for place in places:
    df_pe = pd.read_csv('data/covid19-' + place + '.csv')
    df_pe['date'] = pd.to_datetime(df_pe['date'], yearfirst=True, format='%Y-%m-%d')

    plt.figure(figsize=(16,9))
    my_bar(df_pe, 'confirmed')
    plt.legend(['Novos casos confirmados em ' + str.upper(place)])
    plt.title('Novos casos diários de COVID19')
    plt.savefig('figs/novos_casos_' + place + '.png')

    plt.figure(figsize=(16,9))
    my_plot(df_pe, 'confirmed')
    my_plot(df_pe, 'deaths', fmt='-+')
    plt.legend(['Confirmados em ' + str.upper(place), 'Mortes em ' + str.upper(place)])
    plt.title('Casos de COVID19')
    plt.savefig('figs/casos_' + str(place) + '.png')

    plt.figure(figsize=(16,9))
    my_plot(df_pe, 'confirmed_per_100k_inhabitants')
    plt.legend(['Confirmados por 100 mil habitantes em ' + str.upper(place)])
    plt.title('Casos por 100 mil de COVID19')
    plt.savefig('figs/casos_100k_' + str(place) + '.png')
    
    plt.figure(figsize=(16,9))
    my_plot(df_pe, 'death_rate', '-+')
    plt.legend(['Taxa de mortalidade em ' + str.upper(place)])
    plt.title('Mortalidade da COVID19')
    plt.savefig('figs/mortalidade_' + str(place) + '.png')

plt.show()
