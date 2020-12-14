from django.shortcuts import render, get_object_or_404, redirect

from .models import Question, Module


def welcome(request):
    """Generates a welcome page explaining the modumat

    :param request:
    :return:
    """
    return render(request, 'modumat_app/welcome.html')


def question(request, question_id: int):
    """Generates a question page giving the user the option to answer them

    :param request:
    :param question_id:
    :return:
    """
    requested_question = get_object_or_404(Question, pk=question_id)
    all_questions = Question.objects.all()
    next_page_results = (requested_question.next_question() is None)

    next_question_pk = None
    if not next_page_results:
        next_question_pk = requested_question.next_question().pk

    given_answer = request.session.get(str(requested_question.pk), None)

    return render(request, 'modumat_app/question.html',
                  {
                      'requested_question': requested_question,
                      'next_question': next_question_pk,
                      'all_questions': all_questions,
                      'next_page_results': next_page_results,
                      'given_answer': given_answer,
                  })


def answer(request, question_id):
    """Accepts the form answer for a specified question
    and redirects to the next page specified by the next url argument

    :param request:
    :param question_id:
    :return:
    """
    request.session[question_id] = request.POST['approval']
    next_url = request.GET["next"]
    return redirect(f"{next_url}", permanent=False)


def results(request):
    """Shows a results page with recommended modules

    :param request:
    :return:
    """

    agreement_points = []
    max_agreement_points = Question.objects.count() * 2

    for module in Module.objects.all():
        agreement = module.calculateAgreementPoints(request.session)
        percentage = int(agreement / max_agreement_points * 100)
        agreement_points.append((module, agreement, percentage))

    agreement_points.sort(key=lambda m: m[1], reverse=True)

    return render(request, 'modumat_app/results.html', {
        'module_agreement': agreement_points,
        'max_agreements_points': max_agreement_points,
    })
