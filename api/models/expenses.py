import datetime

from django.db import models
# from django.contrib.auth.models import User
from .profile import Profile

#Expenses model:
#  Fields:
#   userId:(one to one with the Profile table)
#   date
#   value
#   description
#   tag
class Expenses(models.Model):
    user = models.OneToOneField(Profile,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
    value = models.IntegerField(blank=False)
    description = models.CharField(max_length=200, blank=False)
    date = models.DateField()
    #TODO:ADD TAG
