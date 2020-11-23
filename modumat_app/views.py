from django.shortcuts import render, get_object_or_404, redirect

from .models import Question


def question(request, question_id: int):
    requested_question = get_object_or_404(Question, pk=question_id)
    all_questions = Question.objects.all()
    next_page_results = (requested_question.next_question() is None)

    if next_page_results:
        return render(request, 'modumat_app/question.html',
                      {
                          'requested_question': requested_question,
                          'all_questions': all_questions,
                          'next_page_results': next_page_results,
                      })

    return render(request, 'modumat_app/question.html',
                  {
                      'requested_question': requested_question,
                      'next_question': requested_question.next_question().pk,
                      'all_questions': all_questions,
                      'next_page_results': next_page_results,
                  })


def answer(request, question_id):
    request.session[question_id] = request.POST['approval']
    next_url = request.GET["next"]
    return redirect(f"{next_url}", permanent=False)
