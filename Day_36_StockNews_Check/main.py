import requests
import smtplib

with open("secret.txt", "r") as file:
    new_file = file.readlines()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
TICKER_EP = "https://www.alphavantage.co/query"
NEWS_EP = "https://newsapi.org/v2/everything"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : new_file[1]
}

response = requests.get(TICKER_EP, params=parameters)
response.raise_for_status()
stock_data = response.json()

current_data = float(stock_data["Time Series (Daily)"]["2025-07-29"]["4. close"])
yesterday_data = float(stock_data["Time Series (Daily)"]["2025-07-28"]["4. close"])

#check 5% of yesterday's price
price_diff = current_data - yesterday_data
percentage_diff = round((price_diff / yesterday_data) * 100)
print(percentage_diff)

if percentage_diff > 0:
    up_down = "⬆️"
elif percentage_diff < 0:
    up_down = "⬇️"

if abs(percentage_diff) >= 1:
    news_parameters = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apiKey": new_file[3]
    }

    news_data = requests.get(NEWS_EP, params=news_parameters)
    articles = news_data.json()["articles"]
    three_articles = articles[:3]

    story_list = [(f"{COMPANY_NAME}: '{percentage_diff}%{up_down}'"
                   f"\nHeadline: {article['title']}\n Story: {article['description']}") for article in three_articles]


    DUMMY_MAIL = "babzie_python@gmail.com"
    DUMMY_PASSWORD = "broski5639$%%#@b_"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=DUMMY_MAIL, password=DUMMY_PASSWORD)
        for message in story_list:
            connection.sendmail(from_addr=DUMMY_MAIL, to_addrs="facebook@gmail.com", msg=f"Subject: {COMPANY_NAME}\n\n{message}")

