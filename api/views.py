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

        def scrape(request):

            def dictate(dic, key_name):
                d = MyDict()
                tag_lists = ['h3', 'p', 'li', 'pre']

                for tag in tag_lists:
                    s = dic.find_all(tag)    
                    if s:
                        for count in range(len(s)):
                            s[count] = s[count].text
                        d[key_name][tag] = s

                return d


            # post data
            dic = {
                'contest': request.POST.get('contests'),
                'number': request.POST.get('numbers'),
                'question': request.POST.get('questions'),
                }

            # scraping
            scraping_url = "https://atcoder.jp/contests/" + dic['contest'] + dic['number'] + "/tasks/" + dic['contest'] + dic['number'] + "_" + dic['question']
            res = requests.get(scraping_url).text
            soup = BeautifulSoup(res, "html.parser")
            scraped_html = soup.find("div", id="task-statement").find("span", class_="lang-ja").find_all("div", class_="part")
            scraped_html_length = len(scraped_html)

            # assign the values to dic
            dic['url'] = scraping_url
            dic['length'] = scraped_html_length
            innum = outnum = 1
            for i in range(scraped_html_length):
                if i == 0:
                    dic.update(dictate(scraped_html[i], 'statement'))
                elif i == 1:
                    dic.update(dictate(scraped_html[i], 'constraint'))
                elif i == 2:
                    dic.update(dictate(scraped_html[i], 'input'))
                elif i == 3:
                    dic.update(dictate(scraped_html[i], 'output'))
                else:
                    if i % 2 == 0:
                        dic.update(dictate(scraped_html[i], 'insample'+str(innum)))
                        innum += 1
                    else:
                        dic.update(dictate(scraped_html[i], 'outsample'+str(outnum)))
                        outnum += 1

            return dic
        
        template_name = "show_question.html"
        context = scrape(request)
        
        return render(request, template_name, context)