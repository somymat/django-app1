from django.db import models
from basicApp.settings import DATABASES
from mongoengine import *
import datetime
connect(DBNAME)
# Create your models here.
class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)