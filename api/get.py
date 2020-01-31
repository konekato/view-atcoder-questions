import requests
from django.views.generic import TemplateView
from bs4 import BeautifulSoup

from views import ShowQuestion
get = ShowQuestion.get()

contest = get['contest']
number = get['number']
question = get['question']

url = "https://atcoder.jp/contests/" + contest + number + "/tasks/" + contest + number + "_" + question

print(url)

# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# # print(soup.prettify())

# body = soup.find("div", id="task-statement").find("span", class_="lang-ja").find_all("div", class_="part")

# length = len(body)

# # print(body)