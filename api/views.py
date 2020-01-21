from django.shortcuts import render
from django.views.generic import TemplateView



class SelectQuestions(TemplateView):
    template_name = "select_questions.html"

class ShowQuestion(TemplateView):
    template_name = "show_question.html"

    def show(self, request, *args, **kwargs):
        context = super(ShowQuestion, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)