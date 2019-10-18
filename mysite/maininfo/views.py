from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader, RequestContext
from django.urls import reverse
from django.utils import timezone

from .forms import OpinionForm
from .models import Question, Choice


def mainPage(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request,'maininfo/main.html', context)

def questionPage(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'maininfo/questions.html', context)

def opinionPage(request):
    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            op = form.save(commit=False)
            op.date = timezone.now()
            op.save()
            return redirect('maininfo:main')
    else:
        form = OpinionForm()
    return render(request, 'maininfo/opinions.html',{'form': form})

def detail(request, id):
    question = Question.objects.get(pk = id)
    context = {'question': question}
    return render(request,'maininfo/detail.html', context)

def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'maininfo/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('maininfo:results', args=(question.id,)))


def results(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'maininfo/results.html', {'question': question})