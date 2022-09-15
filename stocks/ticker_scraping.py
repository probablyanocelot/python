import bs4 as bs
import datetime as dt
import os
from pandas_datareader import data as pdr
import pandas_datareader.data as web
import pickle
import requests
import yfinance as yf

yf.pdr_override()

#use on all major indices
def save_sp500_tickers():
	resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup = bs.BeautifulSoup(resp.text, 'lxml')
	table = soup.find('table', {'class': 'wikitable sortable'})
	tickers = []
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text.strip('\n')
		mapping = str.maketrans('.','-')
		ticker = ticker.translate(mapping)
		tickers.append(ticker)

	with open("sp500tickers.pickle", "wb") as f:
		pickle.dump(tickers, f)

	print(tickers)

	return tickers

save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):

	if reload_sp500:
		tickers = save_sp500_tickers()
	else:
		with open("sp500tickers.pickle", "rb") as f:
			tickers = pickle.load(f)

	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')

	start = dt.datetime(2000,1,1)
	end = dt.datetime.date(dt.datetime.today())

	for ticker in tickers:
		print(ticker)
		if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
			df = pdr.get_data_yahoo(ticker, start, end)
			df.reset_index(inplace=True)
			df.set_index("Date", inplace=True)
			df.to_csv('stock_dfs/{}.csv'.format(ticker))
		else:
			print('Already have {}'.format(ticker))

get_data_from_yahoo()

