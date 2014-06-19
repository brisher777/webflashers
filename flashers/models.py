from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User)
    category = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    created = models.DateTimeField('date created', auto_now=True)

    def __unicode__(self):
        return self.category
