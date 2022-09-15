from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox() 
page = driver.get('http://poe.trade/')

# select_search = driver.find_element_by_value('Search!')
select_search =  driver.find_element_by_xpath("//input[@accesskey='s']")
select_search.send_keys(Keys.RETURN)

sleep(3)

item_search = driver.find_element_by_class_name("search-results")

sleep(3)

for item in item_search:
    print(item.text)



# --- HOW TO WAIT AND PRINT ---
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # ...

# wait = WebDriverWait(driver, 100)

# wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'listing-item__title')))
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'listing-item__price')))

# for elm in driver.find_elements_by_css_selector(".listing-item__title,.listing-item__price"):
#     print(elm.text)