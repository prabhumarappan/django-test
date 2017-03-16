from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.core.urlresolvers import reverse

def index(request):
	lastest_questions = Question.objects.order_by('-pub_dates')[:5]
	return render(request,"polls/index.html",{'questions':lastest_questions})

def detail(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,"polls/details.html",{'question':question})

def result(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,"polls/results.html",{'question':question})

def vote(request,question_id):
	p = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,"polls/details.html",{
			'question':p,
			'error_message':"You didn't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:result',args=(p.id,)))
