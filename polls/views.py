# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import *
from .forms import QuestionForm
from django.utils import timezone


# An example of explicit loading
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list, }
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)


# Create a poll question
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            url = reverse('polls:index')
            return HttpResponseRedirect(url)
    else:
        form = QuestionForm()

    return render(request, 'polls/question.html', {'form': form})


# An example of render
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


# An example of get_object_or_404
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
