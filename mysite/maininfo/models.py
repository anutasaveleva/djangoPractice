from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question

    question = models.CharField(max_length=200)

class Opinion(models.Model):
    opinion = models.CharField(max_length=1000)
    date = models.DateTimeField()


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    refers_to = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=140)
    correct = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)