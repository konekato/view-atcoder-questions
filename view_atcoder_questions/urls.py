from django.contrib import admin
from django.urls import path

import api.views as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', api.SelectQuestions.as_view()),
    path('home/question/', api.ShowQuestion.as_view())
]
