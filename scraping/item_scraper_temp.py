#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:17:11 2018
@author: kerry
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv

# USE XPATHS

# specify the url
unique_by_type_urlpage =  'https://poedb.tw/us/unique.php?query=' 
all_uniques = 'https://poedb.tw/us/unique.php?l=1'
print(all_uniques)
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(all_uniques)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
# find results within table
item_sections = soup.find_all('div', attrs={'class': 'card'})
print(item_sections)
# item_type_names = item_sections.find('h5')
table = item_sections.find('tbody')
# table = soup.find('table', attrs={'class': 'tableSorter'})
# table = soup.find('table', attrs={'class': 'tablesorter'})
# print(table)
# item_rows = table.find_all('tr')

# results = table.find_all('tr')
print('Number of items PUT SOMETHING HERE')

# create and write headers to a list 
rows = []
item_dict = {'items':{}}
# rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])

# loop over results
for item in item_rows:
    # find all columns per result
    data = item.find_all('td')
    # check that columns have data 
    if len(data) == 0: 
        continue
    
    rows.append(data)
    # rows.append(data)
    
    # write columns to variables
    # rank = data[0].getText()
    # company = data[1].getText()
    # location = data[2].getText()
    # yearend = data[3].getText()
    # salesrise = data[4].getText()
    # sales = data[5].getText()
    # staff = data[6].getText()
    # comments = data[7].getText()
    
    # print('Company is', company)
    # Company is WonderblyPersonalised children's books
    # print('Sales', sales)
    # Sales *25,860

    # extract description from the name
    # companyname = data[1].find('span', attrs={'class':'company-name'}).getText()    
    # description = company.replace(companyname, '')
    
    # remove unwanted characters
    # sales = sales.strip('*').strip('†').replace(',','')
    
    # go to link and extract company website
    # url = data[1].find('a').get('href')
    # page = urllib.request.urlopen(url)
    # parse the html using beautiful soup and store in variable 'soup'
    # soup = BeautifulSoup(page, 'html.parser')
    # find the last result in the table and get the link
    # try:
    #     tableRow = soup.find('table').find_all('tr')[-1]
    #     webpage = tableRow.find('a').get('href')
    # except:
    #     webpage = None
    
    # write each result to rows
    # rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])


print(rows)

    
## Create csv and write rows to output file
with open('iteminfo.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)