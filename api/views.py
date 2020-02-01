from django.shortcuts import render
from django.views.generic import TemplateView

import requests
from bs4 import BeautifulSoup

from .forms import *

class SelectQuestions(TemplateView):
    def select_questions(request):
        template_name = "select_questions.html"
        context = {'form': ViewContests(),}
        return render(request, template_name, context)

class ShowQuestion(TemplateView):
    def show(request):
        template_name = "show_question.html"

        def scraping(request):
            # post data
            d = {
                'contest': request.POST.get('contests'),
                'number': request.POST.get('numbers'),
                'question': request.POST.get('questions'),
                }
            contest = d['contest']
            number = d['number']
            question = d['question']

            # scraping
            url = "https://atcoder.jp/contests/" + contest + number + "/tasks/" + contest + number + "_" + question
            res = requests.get(url).text
            soup = BeautifulSoup(res, "html.parser")
            h = soup.find("div", id="task-statement").find("span", class_="lang-ja").find_all("div", class_="part")
            length = len(h)
            html = []
            for i in range(length):
                html.append(h[i].text)

            # assign html to d
            oddn = even = 1
            for i in range(length):
                if i == 0:
                    d['statement'] = html[i]
                elif i == 1:
                    d['constraint'] = html[i]
                elif i == 2:
                    d['input'] = html[i]
                elif i == 3:
                    d['output'] = html[i]
                else:
                    if i % 2 == 0:
                        d['insample'+str(oddn)] = html[i]
                        oddn += 1
                    else:
                        d['outsample'+str(even)] = html[i]
                        even += 1

            return d
        
        context = scraping(request)

        print(context)
        
        return render(request, template_name, context)