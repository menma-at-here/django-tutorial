import datetime
from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
  def __str__(self) -> str:
    return self.question_text

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  question_text = models.CharField('question text', max_length=200)
  pub_date = models.DateTimeField('data published')

class Choice(models.Model):
  def __str__(self) -> str:
    return self.choice_text

  question = models.ForeignKey(Question, on_delete=models.CASCADE) #1対多をこれで表現
  choice_text = models.CharField('choice text',max_length=200)
  votes = models.IntegerField('votes',default=0)