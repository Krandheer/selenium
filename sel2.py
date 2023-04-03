from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='/Users/randheerkumar/Downloads/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.in/')
driver.maximize_window()

time.sleep(5)

select = driver.find_element(By.LINK_TEXT, 'Electronics')
select.click()

time.sleep(5)
