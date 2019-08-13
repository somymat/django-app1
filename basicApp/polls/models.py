from django.db import models
from djongo import models
from basicApp.settings import DATABASES
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200,null=True)
    pub_date = models.DateTimeField('date published',null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    choice_text = models.CharField(max_length=200,null=True)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text