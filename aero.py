import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.isdir('figs/aero'):
    os.mkdir('figs/aero')

df_aero = pd.read_csv('data/movimento_passageiros_aero_2018.csv', sep=';')
df_place = pd.read_csv('data/aero_place.csv', sep=';')
df_br = pd.read_csv('data/covid19-' + 'brasil' + '.csv')
df_br['date'] = pd.to_datetime(df_br['date'], yearfirst=True, format='%Y-%m-%d')

print(df_aero.info())
print(df_aero.head())
print(df_place.info())
print(df_place.head())

plt.bar(df_aero['Sigla'], df_aero['Total'])
plt.tick_params(axis='x', labelrotation=90)
plt.savefig('figs/aero/passageiros_aeroporto.png')
states = df_place['UF'].unique()

df_estado = pd.DataFrame(columns=['UF', 'Passageiros', 'Casos'])
for state in states:
    aeros = df_place[df_place['UF'] == state]['ICAO']
    total_state = 0
    casos = df_br[(df_br['is_last']) & (df_br['state'] == state)]['last_available_confirmed'].array[0]
    for aero in aeros:
        total_state += df_aero[df_aero['Sigla'] == aero]['Total'].array[0]

    df_estado = pd.concat([pd.DataFrame([[state, total_state, casos]], columns=['UF', 'Passageiros', 'Casos']), df_estado], ignore_index=True)

print(df_estado.head(10))
df_estado['Passageiros'] = df_estado['Passageiros'].astype(int)
df_estado['Casos'] = df_estado['Casos'].astype(int)
print(df_estado.info())

plt.figure()
df_estado.sort_values(by='Passageiros', inplace=True, ascending=False)
plt.bar(df_estado['UF'], df_estado['Passageiros'])
plt.savefig('figs/aero/passageiros_estados.png')
plt.close()

plt.figure()
plt.scatter(df_estado['Passageiros'], df_estado['Casos'])
for line in range(len(df_estado)):
    plt.text(df_estado.iloc[line]['Passageiros'], df_estado.iloc[line]['Casos'],
            df_estado.iloc[line]['UF'])
plt.ylabel('Casos')
plt.xlabel('Passageiros')
plt.title('Passageiros 2018 x Casos COVID19')
plt.savefig('figs/aero/passageirosXCasos.png')
print(df_estado.corr())
plt.close()