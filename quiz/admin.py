from django.contrib import admin

# Register your models here.

from django.contrib import admin
from quiz.models import Quiz, Question
admin.site.register(Quiz)
admin.site.register(Question)