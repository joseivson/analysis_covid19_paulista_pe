
import matplotlib.pyplot as plt
import numpy as np

apply_log = False

def scale(x):
    if apply_log:
        return np.log10(x)
    else:
        return x

def my_plot(df, column, fmt='-o', print_label=True):
    plt.plot_date(df[df[column] > 0]['date'], df[df[column] > 0][column].apply(scale), xdate=True, fmt=fmt)
    for i,d in zip(df.iloc[:1]['date'], df.iloc[:1][column]):
        plt.text(i, d, str(d))
    plt.tick_params(axis='x', labelrotation=90, left=True)
    # plt.xticks(ticks=df['date'])

def my_bar(df, column):
    new_daily = df.iloc[:-1][column].array-df.iloc[1:][column].array
    plt.bar(df.iloc[:-1]['date'], new_daily, color='b')
    plt.bar(df.iloc[-1]['date'], df.iloc[-1][column], color='b')
    plt.tick_params(axis='x', labelrotation=90, left=True)
    plt.xticks(ticks=df['date'])