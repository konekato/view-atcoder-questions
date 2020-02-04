from django.shortcuts import render
from django.views.generic import TemplateView

import requests
from bs4 import BeautifulSoup

from .forms import *

class MyDict(dict):
    def __missing__(self,key):
        v = self[key] = type(self)()
        return v

class SelectQuestions(TemplateView):
    def select_questions(request):
        template_name = "select_questions.html"
        context = {'form': ViewContests(),}
        return render(request, template_name, context)

class ShowQuestion(TemplateView):
    def show(request):
        template_name = "show_question.html"

        def scrape(request):
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

            def dictate(scraped_dic, key_name):
                dic = MyDict()
                tag_lists = ['h3', 'p', 'li', 'pre']

                for tag in tag_lists:
                    s = scraped_dic.find_all(tag)
                    if s:
                        for count in range(len(s)):
                            dic[key_name][tag][count] = s[count]

                return dic

            # assign the values to d
            d['url'] = url
            d['length'] = length
            innum = outnum = 1
            for i in range(length):
                if i == 0:
                    d.update(dictate(h[i], 'statement'))
                elif i == 1:
                    d.update(dictate(h[i], 'constraint'))
                elif i == 2:
                    d.update(dictate(h[i], 'input'))
                elif i == 3:
                    d.update(dictate(h[i], 'output'))
                else:
                    if i % 2 == 0:
                        d.update(dictate(h[i], 'insample'+str(innum)))
                        innum += 1
                    else:
                        d.update(dictate(h[i], 'outsample'+str(outnum)))
                        outnum += 1

            print(d)

            html = []
            for i in range(length):
                html.append(h[i].text)

            # assign the values to d
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
                        
                    else:
                        d['outsample'+str(even)] = html[i]
                        

            return d
        
        context = scrape(request)
        
        return render(request, template_name, context)