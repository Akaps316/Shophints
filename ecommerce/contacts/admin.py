from django.db import models
from django.contrib import admin
from .models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'



admin.site.register(Feedback, FeedbackAdmin)

