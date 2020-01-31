import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from bs4 import BeautifulSoup

class Scraping(TemplateView):
    def print_url(request, self):
        def dictionary():
            d = {
                'contest': request.POST.get('contests'),
                'number': request.POST.get('numbers'),
                'question': request.POST.get('questions'),
                }
            return d
        get = dictionary()

        contest = get['contest']
        number = get['number']
        question = get['question']

        url = "https://atcoder.jp/contests/" + contest + number + "/tasks/" + contest + number + "_" + question
        print(url)

        return get





# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# # print(soup.prettify())

# body = soup.find("div", id="task-statement").find("span", class_="lang-ja").find_all("div", class_="part")

# length = len(body)

# # print(body)