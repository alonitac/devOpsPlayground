import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\chromedriver.exe")
driver.get('https://www.facebook.com/')
driver.find_element_by_id("email")
driver.get_log('browser')