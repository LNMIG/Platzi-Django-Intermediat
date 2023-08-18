from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

def index(request):
    # return HttpResponse('Estás viendo la página principal')
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse(f'Estás viendo la pregunta número {question_id}')
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def result(request, question_id):
    # return HttpResponse(f'Estás viendo los resultados de la pregunta número {question_id}')
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/result.html', context)


def vote(request, question_id):
    # return HttpResponse(f'Estás votando a la pregunta número {question_id}')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question, 'error_message': 'No elegiste una opción'}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('apps.polls:result', args=(question.id,)))