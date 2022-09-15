import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import pickle
import os, os.path
import glob



# Time Range For Data
#  --Make This Find Start Based on Stock--
start = dt.datetime(2000, 1, 1)
end = dt.datetime.date(dt.datetime.today())


# Grabs Data
def ticker(ticker_str):
	df = web.DataReader(ticker_str, 'yahoo', start, end)
	return df
# print(ticker('TSLA').tail())


# Data To CSV
# ticker('TSLA').to_csv('tsla.csv')
def store_ticker(ticker_str):
	ticker(ticker_str).to_csv(ticker_str+'.csv')
# store_ticker('MSFT')


# Data From CSV
def read_stored_ticker(ticker_str):
	df = pd.read_csv(ticker_str+'.csv', parse_dates=True, index_col=0)
	return df
# print(read_stored_ticker('TSLA').head())


# Read Pickle File
def read_pickle(pickle_file, list1):
	with (open(glob.glob('./**/' + pickle_file + '.csv'), "rb")) as openfile:
		while True:
			try:
				list1.append(pickle.load(openfile))
				return list1
			except EOFError:
				break