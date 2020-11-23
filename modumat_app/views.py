from django.shortcuts import render, get_object_or_404, redirect

from .models import Question


def question(request, question_id: int):
    requested_question = get_object_or_404(Question, pk=question_id)
    all_questions = Question.objects.all()
    return render(request, 'modumat_app/question.html',
                  {
                      'requested_question': requested_question,
                      'next_question': requested_question.pk + 1, #TODO: Replace with actual next question
                      'all_questions': all_questions
                  })


def answer(request, question_id):
    request.session[question_id] = request.POST['approval']
    next_question_id = request.GET["next_question"]
    return redirect(f"/question/{next_question_id}", permanent=False)
