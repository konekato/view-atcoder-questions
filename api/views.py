from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import *

class SelectQuestions(TemplateView):
    def select_questions(request):
        template_name = "select_questions.html"
        c = {'form': ViewContests(),}
        return render(request, template_name, c)

class ShowQuestion(TemplateView):
    template_name = "show_question.html"

    def show(self, request, *args, **kwargs):
        context = super(ShowQuestion, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)