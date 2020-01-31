from django.contrib import admin
from django.urls import path

import api.views as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', api.SelectQuestions.select_questions),
    path('home/question/', api.ShowQuestion.show)
]
