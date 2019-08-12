from django.shortcuts import render
from django.http import HttpResponce
from .models import Question
from django.template import loader


# Create your views here.
def detail(request, question_id):((
    return HttpResponce("you are looking at the questions {}", .format("question_id"))
def results(request, question_id):
    return HttpResponce("you are looking at the result of the question {}",.format("question_id"))
def vote(request, question_id):
    return HttpResponce("you are voting on question {}",.format("question_id"))
def index(request):
    latestQues=Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    output = ','.join([q.question_text for q in latestQues])
    context = {'latestQues': latestQues}
    return render(request, 'polls/index.html', context), output