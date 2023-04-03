from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# set up Chrome WebDriver
service = Service(executable_path='/Users/randheerkumar/Downloads/chromedriver_mac64/chromedriver')
driver = webdriver.Chrome(service=service)

# navigate to MagicBricks website
driver.get("https://www.magicbricks.com/")

# wait for page to load
time.sleep(5)

# locate search input box and input search query
driver.find_element(By.ID, "tabBUY")
search_box = driver.find_element(By.ID, "keyword")
search_box.clear()
search_box.send_keys("Bangalore")
search_box.click()
time.sleep(10)
# press enter to search
# search_box.send_keys(Keys.RETURN)
# print(search_box.send_keys(Keys.RETURN))
#
# # wait for search results to load
# time.sleep(10)
#
# # locate and click on "Buy" filter
# buy_filter = driver.find_element(By.XPATH, "//label[@for='buy']")
# buy_filter.click()
#
# # wait for search results to update
# time.sleep(5)
#
# # locate and click on "Residential" filter
# residential_filter = driver.find_element(By.XPATH, "//label[@for='residential']")
# residential_filter.click()
#
# # wait for search results to update
# time.sleep(5)
#
# # get all the listing elements on the page
# listings = driver.find_elements(By.XPATH, "//div[@class='flex relative clearfix m-srp-card__container']")
#
# # scrape data from each listing
# for listing in listings[:90]:
#     # extract details of each listing
#     title = listing.find_element(By.CLASS_NAME, "m-srp-card__title").text
#     price = listing.find_element(By.CLASS_NAME, "m-srp-card__price").text
#     area = listing.find_element(By.CLASS_NAME, "m-srp-card__area").text
#     location = listing.find_element(By.CLASS_NAME, "m-srp-card__address").text
#     details = listing.find_element(By.CLASS_NAME, "m-srp-card__summary__item").text
#
#     # print the extracted details
#     print("Title:", title)
#     print("Price:", price)
#     print("Area:", area)
#     print("Location:", location)
#     print("Details:", details)
#     print("--------------------")

# close the browser window
driver.quit()
