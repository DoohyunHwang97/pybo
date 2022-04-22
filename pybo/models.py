from django.db import models
from django import forms

# Create your models here.
class Question(models.Model):

    def __str__(self):
        return self.subject

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):

    def __str__(self):
        return self.subject
    subject = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]
