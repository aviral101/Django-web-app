from django.db import models

# Create your models here.

class Notification(models.Model):
    notificationtext=models.TextField()
    posteddate=models.CharField(max_length=30)
class Knowledgebase(models.Model):
    problemid=models.CharField(max_length=20)
    problemtext=models.TextField()
    solutiontext=models.TextField()
    posteddate=models.CharField(max_length=30)
