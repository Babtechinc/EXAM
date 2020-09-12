from django.db import models

# Create your models here.
class exam(models.Model):
    question = models.CharField(blank=None,max_length=1000)
    answer = models.CharField(blank=None,max_length=1000)
    option1 = models.CharField(blank=None, max_length=1000)
    option2 = models.CharField(blank=None, max_length=1000)
    option3 = models.CharField(blank=None, max_length=1000)
    option4 = models.CharField(blank=None, max_length=1000)
    def __str__(self):
        return self.question