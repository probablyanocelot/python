from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

firefox = webdriver.Firefox()
pages = {}
url = 'http://poe.trade/'


class SelCrawler:

    def __init__(self, driver, target):
        self.driver = driver
        self.target = target
    
    def first_page(self):
        self.driver.get(self.target)

    # add search box input
    def search(self, search_term_str):
        if search_term_str:
          query = self.driver.find_element_by_xpath("//input[@name='name']")
          query.send_keys(str(search_term_str))
        sleep(3)
        select_search = self.driver.find_element_by_xpath("//input[@accesskey='s']")
        select_search.send_keys(Keys.RETURN)

poe = SelCrawler(driver=firefox, target=url)
poe.first_page()
poe.search("Primordial")
# class PoEselCrawler(selCrawler):
#     PoEselCrawler.crawl_driver = firefox
#     PoEselCrawler.page = url

# selCrawler(firefox, url)
# first_page(set_driver(firefox), 'http://poe.trade/')
# select_search = driver.find_element_by_value('Search!')
# select_search =  driver.find_element_by_xpath("//input[@accesskey='s']")
# select_search.send_keys(Keys.RETURN)


'''class Car(): 

  def __init__(self, model): 
    self.model = model
  		
  def brand(self): 
    print("The brand is", self.model)  

if __name__ == "__main__":
  car = Car("Bmw")
  car.brand()
'''