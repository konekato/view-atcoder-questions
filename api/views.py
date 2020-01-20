from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

class SelectQuestions(TemplateView):
    template_name = "select_questions.html"
