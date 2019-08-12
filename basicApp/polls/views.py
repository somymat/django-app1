from django.shortcuts import render
from django.http import HttpResponce


# Create your views here.
def detail(request, question_id):((
    return HttpResponce("you are looking at the questions {}", .format("question_id"))
def results(request, question_id):
    return HttpResponce("you are looking at the result of the question {}",.format("question_id"))
def vote(request, question_id):
    return HttpResponce("you are voting on question {}",.format("question_id"))