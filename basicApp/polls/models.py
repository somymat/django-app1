from django.db import models
from djongo import models
from basicApp.settings import DATABASES
import datetime

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    choice_text = models.CharField(max_length=200,null=True)
    votes = models.IntegerField(default=0)