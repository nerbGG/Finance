from django.db import models
from django.contrib.auth.models import User

#Profile model:
#  Fields: user (one to one with the User table)
#  the name of an object will be the object's username
class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
    def __str__(self):
        return self.user.username +" 's profile"
