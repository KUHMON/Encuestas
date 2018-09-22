#  appEncuestas/views.py
# version Django 2.1

from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'appEncuestas/index.html', context)

    
def index2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('appEncuestas/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))	

def indexBasico(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
	

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'appEncuestas/detail.html', {'question': question})

	
def detailAnterior(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def resultsAnterior(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)
	
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'appEncuestas/results.html', {'question': question})

def voteAnterior(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
	
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'appEncuestas/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('espacioEncuestas:results', args=(question.id,)))		
	
	
