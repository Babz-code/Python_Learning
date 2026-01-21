from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

event_link = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

event_dict = {i: {"date": event_date[i].text, "name": event_link[i].text} for i in range(len(event_link))}
print(event_dict)



driver.quit()
