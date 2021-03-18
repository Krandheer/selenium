from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = '/Users/randheerkumar/Downloads/chromedriver')
driver.get('http://www.google.com')

driver.maximize_window()

input=driver.find_element_by_name('q')
input.send_keys('facebook.com')
time.sleep(5)

button = driver.find_element_by_name('btnK')
button.click()
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.quit()