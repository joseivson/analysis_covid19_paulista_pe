import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import pandas as pd
from datetime import timedelta

def gaussian(x, mean, std):
    return np.exp((x-mean)**2/(2*std**2))

def concat_invert(x):
    y = np.concatenate((x, np.transpose(x)))
    return y

def project_new_cases(df, column='new_confirmed'):
    df.sort_values(by='date', ascending=True, inplace=True)
    new_confirmed = df[column].array
    peaks = find_peaks(new_confirmed)
    plt.bar(df['date'], new_confirmed)
    plt.scatter(df.iloc[peaks[0]]['date'], new_confirmed[peaks[0]])
    z = np.polyfit(peaks[0], np.array(new_confirmed[peaks[0]]), 3)
    p = np.poly1d(z)
    plt.plot(df.iloc[peaks[0]]['date'], p(peaks[0]))
    inter_days = (df['date'].max()-df['date'].min()).days
    y = p(np.arange(inter_days-1,inter_days+45))
    inter_days = int(sum(y>=0))
    plt.plot(pd.date_range(df['date'].max()-timedelta(1), df['date'].max()+timedelta(days=inter_days-2)), y[:inter_days])
    plt.show()

if __name__ == '__main__':
    plt.figure()
    df_place = pd.read_csv('data/covid19-pernambuco.csv')
    df_place['date'] = pd.to_datetime(df_place['date'], yearfirst=True, format='%Y-%m-%d')
    project_new_cases(df_place)

    df_place = pd.read_csv('data/covid19-recife.csv')
    df_place['date'] = pd.to_datetime(df_place['date'], yearfirst=True, format='%Y-%m-%d')
    project_new_cases(df_place)

    df_place = pd.read_csv('data/covid19-paulista.csv')
    df_place['date'] = pd.to_datetime(df_place['date'], yearfirst=True, format='%Y-%m-%d')
    project_new_cases(df_place)

    df_world = pd.read_csv('data/owid-covid-data.csv')
    df_world['date'] = pd.to_datetime(df_world['date'], yearfirst=True, format='%Y-%m-%d')
    project_new_cases(df_world[df_world['location']=='China'], column='new_cases')

    plt.show()
    df_sp = df_place[df_place['state']=='SP']

