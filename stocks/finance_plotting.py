# print(ticker('TSLA').tail())
# store_ticker('MSFT')
# print(read_stored_ticker('TSLA').head())
# tickers.read_stored_ticker('KHC').plot()

import tickers as t
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates


# plots input ticker -- will add functionality
def p(ticker_str_or_df):
	if type(ticker_str_or_df) is str:
		t.read_stored_ticker(ticker_str_or_df)['Adj Close'].plot()
	else:
		try:
			ticker_str_or_df.plot()
		except:
			print('uh oh, string or df plz')
	# elif type(ticker_str_or_df) is classmethod:
	# 	ticker_str_or_df.plot()

style.use('ggplot')

print(t.read_stored_ticker('KHC')[['Open','High']].tail())

df = t.read_stored_ticker('KHC')
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# df.dropna(inplace=True) -- EXCLUDES ROWS WITH NA

df_ohlc = df['Adj Close'].resample('10D').ohlc() #10Min, etc. can do .mean(), sum()
print(df_ohlc)
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

print(df_ohlc.tail())




ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

# mpf.plot()
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
#candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g') DEPRECATED
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])
# p(df)

plt.show()

print(type(df))
# ON p.4 https://www.youtube.com/watch?v=19yyasfGLhk&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ&index=4