from django.shortcuts import render
from django.views.generic import TemplateView

class SelectQuestions(TemplateView):
    template_name = "select_questions.html"

class ShowQuestion(TemplateView):
    template_name = "show_question.html"
