from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def question(request, question_id: int):
    requested_question = get_object_or_404(Question, pk=question_id)
    all_questions = Question.objects.all()
    return render(request, 'modumat_app/question.html',
                  {
                      'requested_question': requested_question,
                      'all_questions': all_questions
                  })
