from django.shortcuts import render
from django.views.generic import TemplateView

from forms import *

class SelectQuestions(TemplateView):
    def select_questions(request):
        template_name = "select_questions.html"
        context = {'form': ViewContests(),}
        return render(request, template_name, context)

class ShowQuestion(TemplateView):
    def get():
        # d = {
        #     'contest': request.GET.get('contests'),
        #     'number': request.GET.get('numbers'),
        #     'question': request.GET.get('questions'),
        #     }
        d = {
            'contest': 'abc',
            'number': '1',
            'question': 'A',
            }
        return d
        
    def show(request):
        template_name = "show_question.html"
        context = get()

        return render(request, template_name, context)