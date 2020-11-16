from django.http import Http404
from django.shortcuts import render

from .models import Question


def question(request, question_id: int):
    try:
        requested_question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'modumat_app/question.html', {'requested_question': requested_question})
