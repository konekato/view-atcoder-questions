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

        # scraping
        def scraping(request):
            d = {
                'contest': request.POST.get('contests'),
                'number': request.POST.get('numbers'),
                'question': request.POST.get('questions'),
                }
            contest = d['contest']
            number = d['number']
            question = d['question']

            url = "https://atcoder.jp/contests/" + contest + number + "/tasks/" + contest + number + "_" + question
            print(url)
            return d

        # def get(request):
        #     d = {
        #         'contest': request.POST.get('contests'),
        #         'number': request.POST.get('numbers'),
        #         'question': request.POST.get('questions'),
        #         }
        #     # d = {
        #     #     'contest': 'abc',
        #     #     'number': '1',
        #     #     'question': 'A',
        #     #     }
        #     return d
        
        context = scraping(request)
        
        return render(request, template_name, context)