from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(3)

print("Looking for language selection...")
try:
    choose_lang = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found it. Clicking...")
    choose_lang.click()
    time.sleep(3)

except NoSuchElementException:
    print("Can't find any language")

time.sleep(2)

current_time_seconds_only = time.time()
wait_time = 20
cookie = driver.find_element(By.ID, "bigCookie")

# Get the list of upgrades with their corresponding price
product_list = []
for item in range(0, 6):
    product_name = driver.find_element(By.ID, value=f"productName{item}").text
    product_price = driver.find_element(By.ID, value=f"productPrice{item}").text
    product_list.append((product_name, product_price))

while True:
    cookie.click()
    if time.time() == current_time_seconds_only + wait_time:
        # get current number of cookies
        cookies_amount = driver.find_element(By.ID, value="cookies").text
        print(cookies_amount)

        #  # compare the current number of cookies with the upgrades and get the most expensive one
        # for price in product_list:
        #     if price[1] > cookies_amount:
        #         cookies_amount = price[1]
        #     # buy



# driver.quit()


