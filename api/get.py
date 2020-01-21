import requests
from bs4 import BeautifulSoup

r = requests.get("https://atcoder.jp/contests/abc152/tasks/abc152_c")
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())

body = soup.find("div", id="task-statement").find("span", class_="lang-ja").find_all("div", class_="part")

length = len(body)

print(body)