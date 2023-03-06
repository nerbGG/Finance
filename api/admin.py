from django.contrib import admin
from .models.profile import Profile
from .models.expenses import Expenses

# Register your models here.
admin.site.register(Profile)
admin.site.register(Expenses)