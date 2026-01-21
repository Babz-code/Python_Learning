from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

#Fake mail & password for tryout
DUMMY_EMAIL = "babziecode@gmail.com"
DUMMY_PASSWORD = os.getenv('DUMMY_PASSWORD')

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

website = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(url=website, headers=header)
web_html = response.text

soup = BeautifulSoup(web_html, "lxml")
# print(soup)
whole = soup.find("span", class_="a-price-whole").getText()
cent = soup.find("span", class_="a-price-fraction").getText()

price = float(whole + cent)
title = soup.find("span", id="productTitle").getText()


target_price = 100
if price < target_price:
    with smtplib.SMTP("mail.guerrillamail.com") as connection:
        connection.starttls()
        connection.login(user=DUMMY_EMAIL, password=DUMMY_PASSWORD)
        connection.sendmail(from_addr=DUMMY_EMAIL,
                            to_addrs="facebook@gmail.com",
                            msg=f"Subject: {title}!\n\n This is now at a good price of ${price} and here is the link to get it{website}")





