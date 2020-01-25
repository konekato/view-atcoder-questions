import requests
from bs4 import BeautifulSoup

from forms import *
FORM_NAME_NUMBER = 0

num = 1
contest=CONTESTS[num][FORM_NAME_NUMBER]
number = NUMBERS[num][FORM_NAME_NUMBER]
question = QUESTIONS[num][FORM_NAME_NUMBER]
# 小さく変数化したいcontest=CONTESTS[1][FORM_NAME_NUMBER] みたいな
url = "https://atcoder.jp/contests/" + contest + number + "/tasks/" + contest + number + "_" + question

print(url)

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())

body = soup.find("div", id="task-statement").find("span", class_="lang-ja").find_all("div", class_="part")

length = len(body)

# print(body)