from bs4 import BeautifulSoup
import requests
import re

# CHECK BS4 CODE FOR LIST OF ATTRS

# consumes site html and returns as usable data
def page_to_etree(url):
    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    '''
    convert to etree for xpaths
    dom = etree.HTML(str(soup))
    '''
    return soup


# need to use docs to check if method in bs4 file (if method viable)
# https://github.com/waylan/beautifulsoup/blob/master/bs4/element.py
def crawler(soup):
    # need to enumerate(?) tiers of html to crawl next node

    # parse soup line for line (how)
    for x in soup:
        # ele = list of html elements
        for y in eles:
            if y in x:
                soup_replacement = soup.y
                crawler(soup_replacement)
            elif next_node:
                move_to_next_node
            else:
                print("end of node")


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
  
# @wrapper - try that?
# converts target into soup; quickly make soup out of things like:
# item_weapon_section = soup.find_all('div', id='Uniqueunique_listtitleWeapon')
# default parser = html.parser
class reSoup():

    def __init__(self, target_object, parser_str=None):
        if parser_str is None:
            parser_str = "html.parser"
            self.parser_str = parser_str
        
        soup = BeautifulSoup(str(target_object), parser_str)
        return soup


# CRAWLER -- ALT : USE SCRAPY
    # looks for desired tag by trying list of tags 
    # and narrowing soup after each iteration
class iterSoup():

    counter = []
    count_limit = []

    def __init__(self, soup, count_limit, attr): # attr for attr in attr_list (need elements list)
        killswitch = False

        # sets counter, in case you decide to use it during runtime
        if self.counter is None:
            counter = 0
            self.counter = counter

        # while below count_limit, resoups until it finds element user specifies
        if not killswitch:
            while counter <= count_limit or count_limit is None:
                soup = reSoup(soup)
                for item1 in soup:
                    if item1.attr:
                        print(item1.attr)                     # think item.tbody.tr.td.a
                        counter +=1
                                                                # for item2 in reSoup(item.attr):
                                                                #     if item2.attr:
                                                                #         print(item2.attr)
                    

        if item1.attr:                    # if item2.attr:
            iterSoup(reSoup(item1.attr))    # iterSoup(reSoup(item2.attr))
        else:
            print("not found")
            attr = input("Try another attribute? ** LEAVE BLANK AND PRESS ENTER TO QUIT **\n:")
            iterSoup(reSoup(item1.attr))





# re patterns
heading_pattern = r"\w\s\w"

# URLs
unique_by_type_urlpage = 'https://poedb.tw/us/unique.php?query=' 
all_uniques = 'https://poedb.tw/us/unique.php?l=1'

# dicts
item_category_list = []
weapon_list = []
armour_list = []
other_list = []

# make more universal with for comprehensions
item_dict = {
    'uniques': {}
}

# get webpage
webpage = requests.get(all_uniques, headers=HEADERS)
# read webpage as soup
soup = BeautifulSoup(webpage.content, 'html.parser')
# find all cards, use class_ bc python uses class
item_category_cards = soup.find_all('div', class_='card')
item_weapon_section = soup.find_all('div', id='Uniqueunique_listtitleWeapon')
# iterate over above selected info
counter = 0
for item in item_category_cards:
    if item.h5:
        # use re to strip the '/278'
        item_category = item.h5
        print(item_category.text)
        item_category_list.append(item_category.text)
# print(item_weapon_section



                    # if item.a:
                    #     print(item.a.text)
                    # else:
                    #     print(item.text)
        # else:
        #     continue
            # print(item.tbody.tr.td.a.text)
            # if item.div.div.table.tbody:
            #     print(item.div.div.table.tbody.text)




item_dict['uniques'].update(dict.fromkeys(item_category_list, {}))

        
print(item_dict['uniques'][0])
# print(item_dict['uniques'])
# print(item_dict[0][0][0])
    # print(item.prettify())