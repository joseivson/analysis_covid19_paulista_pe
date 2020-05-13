
import matplotlib.pyplot as plt
import numpy as np

apply_log = False

def scale(x):
    if apply_log:
        return np.log10(x)
    else:
        return x

def my_plot(df, column, fmt='-o', print_label=True, grid=True,date_int=1):
    plt.plot_date(df[df[column] > 0]['date'], df[df[column] > 0][column].apply(scale), xdate=True, fmt=fmt)
    for i,d in zip(df.iloc[:1]['date'], df.iloc[:1][column]):
        plt.text(i, d, str(d))
    plt.tick_params(axis='x', labelrotation=90, left=True)
    if date_int==1:
        plt.xticks(ticks=df['date'])
    plt.grid(b=grid, which='major', axis='x')

def my_bar(df, column, legend, title, fig_name):
    plt.figure(figsize=(16,9))
    plt.bar(df['date'], df[column], color='b')
    plt.tick_params(axis='x', labelrotation=90, left=True)
    plt.xticks(ticks=df['date'])
    plt.grid(b=True, which='major', axis='y')
    plt.legend(legend, loc='upper left')
    plt.title(title)
    plt.savefig(fig_name)
    plt.close()

def compare_places(dfs, column, title, places):
    plt.figure(figsize=(16,9))
    for df in dfs:
        my_plot(df, column)
    plt.title(title)
    plt.legend(places)
    str_place = ''
    for place in places[:-1]:
        str_place += place + 'x'
    str_place += places[-1] 
    plt.savefig('figs/' + title.replace(' ', '_') + '_' + str_place + '.png')
    plt.close()

def insert_division_column(df, name, column1, column2):
    df[name] = df[column1].array / df[column2]

def mean_mobile(x, days):
    y = []
    for d in range(len(x)-days):
        y.append(np.mean(x[d:d+days]))

    return np.array(y)

def percentage(x):
    return x*100

def per_100k(x):
    return x * 100000