import urllib.request as ur
from bs4 import BeautifulSoup
import pandas as pd
import os.path



# Enter a stock symbol
index = 'MSFT'
# URL link
url_is = 'https://finance.yahoo.com/quote/' + index + '/financials?p=' + index
url_bs = 'https://finance.yahoo.com/quote/' + index + '/balance-sheet?p=' + index
url_cf = 'https://finance.yahoo.com/quote/' + index + '/cash-flow?p=' + index

read_data = ur.urlopen(url_is).read()
soup = BeautifulSoup(read_data, 'lxml')

ls = []  # Create empty list
for li in soup.find_all('div'):
    # Find all data structure that is ''div
    ls.append(li.string)  # add each element one by one to the list

ls = [e for e in ls if e not in ('Operating Expenses', 'Non-recurring Events')]  # Exclude those columns

new_ls = list(filter(None, ls))
new_ls = new_ls[12:]


print(new_ls)


is_data = list(zip(*[iter(new_ls)]*6))

income_st = pd.DataFrame(is_data[0:])

income_st.columns = income_st.iloc[0]  # Name columns to first row of dataframe
income_st = income_st.iloc[1:, ]  # start to read 1st row
income_st = income_st.T  # transpose dataframe
income_st.columns = income_st.iloc[0]  # Name columns to first row of dataframe
income_st.drop(income_st.index[0], inplace=True)  # Drop first index row
income_st.index.name = ''  # Remove the index name
income_st.rename(index={'ttm': '12/31/2019'}, inplace=True)  # Rename ttm in index columns to end of the year
income_st = income_st[income_st.columns[:-5]]  # remove last 5 irrelevant columns

print(income_st)

print(income_st['Book Value'])

# income_st.to_csv(index + '.csv')

