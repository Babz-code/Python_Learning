from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     website = file.read()
#
# response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
# yc_news_web = response.text
#
# soup = BeautifulSoup(yc_news_web, "html.parser")
# articles = soup.find_all("a", class_="storylink")
#
# articles_text_list = []
# articles_link_list = []
#
# for article in articles:
#     #Getting the text
#     article_text = article.getText()
#     articles_text_list.append(article_text)
#     #Getting the web address
#     article_link = article.get("href")
#     articles_link_list.append(article_link)
#
# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
# # print(articles_text_list)
# # print(articles_link_list)
# # print(article_upvote)
#
# highest_upvote = max(article_upvote)
# highest_index = article_upvote.index(highest_upvote)
# print(articles_text_list[highest_index])
# print(articles_link_list[highest_index])


# TODO. 1. Scraping empire top 100 movies list
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
title = soup.find_all("h3")

movies_list = [each.getText() for each in title]

for x in range(1, len(movies_list) + 1):
    each_movie = movies_list[-x]
    with open("Movies.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{each_movie}\n")

