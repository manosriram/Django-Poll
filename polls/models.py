from django.db import models


class Question(models.Model):
    questionText = models.CharField(max_length=264)
    publishedDate = models.DateTimeField("Date Published")

    def __str__(self):
        return self.questionText


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText
