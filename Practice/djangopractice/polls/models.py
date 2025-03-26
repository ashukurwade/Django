from django.db import models

# Create your models here.

class Question(models.Model):
    questions_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

class Choice(models.Model):
    questions = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

