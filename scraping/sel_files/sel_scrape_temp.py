from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox() 
page = driver.get('http://poe.trade/')

# select_search = driver.find_element_by_value('Search!')
select_search =  driver.find_element_by_xpath("//input[@accesskey='s']")
select_search.send_keys(Keys.RETURN)