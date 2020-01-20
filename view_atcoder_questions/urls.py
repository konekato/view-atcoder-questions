from django.contrib import admin
from django.urls import path

from api.views import SelectQuestions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', SelectQuestions.as_view())
]
