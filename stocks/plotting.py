import pandas as pd
import pandas_datareader
import read_csv
import matplotlib.pyplot as plt
from matplotlib import style
import re


def do_plot(csv_name_str, ma_period):

    # uses 'Adj Close' for now
    style.use('ggplot')

    df = read_csv.create_df(csv_name_str, True, 0)

    df[str(ma_period)+'ma'] = df['Adj Close'].rolling(window=ma_period,
                                                      min_periods=0).mean()

    # multiple graphs = create sublots, aka axes
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=5, colspan=1, sharex=ax1)
    ax1.plot(df.index, df['Adj Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])
    plt.show()

# do_plot('spy.csv', 100)


style.use('ggplot')

splitDict = {}

pattern = r' : '
with open(r'closestats.txt', "r") as file:
    for line in file:
        s = re.split(pattern, line.strip('\n'))
        splitDict[s[0]] = s[1]


df = pd.Series(splitDict, index=splitDict.keys())
# df.reset_index(name='Cent')

print(df)

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax1.plot(df, df.index)
plt.show()
