from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox()

def set_driver(browser):
    driver = browser
    return driver

def first_page(url):
    page = set_driver().get(url)

set_driver(firefox)
first_page('http://poe.trade/')
# select_search = driver.find_element_by_value('Search!')
select_search =  driver.find_element_by_xpath("//input[@accesskey='s']")
select_search.send_keys(Keys.RETURN)