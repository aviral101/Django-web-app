from django.db import models

# Create your models here.
class Complain(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    complaintext=models.TextField()
    complaindate=models.CharField(max_length=30)
class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    questiontext=models.TextField()
    askedby=models.CharField(max_length=50)
    posteddate=models.CharField(max_length=30)
class Answer(models.Model):
    aid=models.AutoField(primary_key=True)
    answertext=models.TextField()
    answeredby=models.CharField(max_length=50)
    qid=models.IntegerField()
    answereddate=models.CharField(max_length=30)