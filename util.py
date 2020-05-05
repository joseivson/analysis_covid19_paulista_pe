
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

def my_bar(df, column):
    new_daily = df.iloc[:-1][column].array-df.iloc[1:][column].array
    plt.bar(df.iloc[:-1]['date'], new_daily, color='b')
    plt.bar(df.iloc[-1]['date'], df.iloc[-1][column], color='b')
    plt.tick_params(axis='x', labelrotation=90, left=True)
    plt.xticks(ticks=df['date'])

def compare_places(df1, df2, column, title, place1, place2):
    plt.figure(figsize=(16,9))
    my_plot(df1, column)
    my_plot(df2, column)
    plt.title(title)
    plt.legend([place1, place2])
    plt.savefig('figs/' + title.replace(' ', '_') + '_' + place1 + 'x' + place2 + '.png')
    plt.close()

def insert_division_column(df, name, column1, column2):
    df[name] = df[column1].array / df[column2]

def mean_mobile(x, days):
    y = []
    for d in range(len(x)-days):
        y.append(np.mean(x[d:d+days]))

    return np.array(y)