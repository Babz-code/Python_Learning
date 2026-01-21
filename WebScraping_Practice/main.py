import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

website = ("https://www.audiologyonline.com/audiology-jobs/illinois-il/glenview/costco-hearing-aid-centers-dispensing-366913")

response = requests.get(url=website, headers=headers)
html = response.text
print(response.status_code)

soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())
# hi = soup.find("a", class_="jobLink")
# print(hi)

buy = soup.find("a", href="mailto:anthonyzepeda@costco.com")
print(buy.string)

