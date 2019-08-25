from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://www.google.com")

time.sleep(5)

search_box = driver.find_element_by_name('q')

search_box.send_keys('Hello')

search_box.submit()

time.sleep(5)

driver.quit()