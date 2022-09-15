# import libraries
import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
import requests
import csv

# URLs
# unique_by_type_urlpage =  'https://poedb.tw/us/unique.php?query='
# all_uniques = 'https://poedb.tw/us/unique.php?l=1'


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def page_to_etree(URL):
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    return dom

# dom = page_to_etree(all_uniques)
# print(dom)
# print(dom.xpath('//*[@tr]'))
# print(dom.findall('.'))


def example():
    root = ET.fromstring(countrydata)

    # Top-level elements
    root.findall(".")

    # All 'neighbor' grand-children of 'country' children of the top-level
    # elements
    root.findall("./country/neighbor")

    # Nodes with name='Singapore' that have a 'year' child
    root.findall(".//year/..[@name='Singapore']")

    # 'year' nodes that are children of nodes with name='Singapore'
    root.findall(".//*[@name='Singapore']/year")

    # All 'neighbor' nodes that are the second child of their parent
    root.findall(".//neighbor[2]")

    # USE XPATHS

    print(all_uniques)
    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(all_uniques)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    # find results within table
    item_sections = soup.find_all('div', attrs={'class': 'card'})
    print(item_sections)
    item_type_names = item_sections.find('h5')
    print(item_type_names)
    table = item_sections.find_all('tbody')
    table = soup.find('table', attrs={'class': 'tableSorter'})
    table = soup.find('table', attrs={'class': 'tablesorter'})
    print(table)
    item_rows = table.find_all('tr')

    # results = table.find_all('tr')
    print('Number of items PUT SOMETHING HERE')

    # create and write headers to a list
    rows = []
    item_dict = {'items': {}}
    rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location',
                'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])
