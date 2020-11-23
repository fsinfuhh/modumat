from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('question/<int:question_id>', views.question, name='question'),
    path('answer/<int:question_id>', views.answer, name='answer'),
]