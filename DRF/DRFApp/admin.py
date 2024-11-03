from django.contrib import admin
from . models import DRFQuest


# Register your models here.
@admin.register(DRFQuest)
class DRFQuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'course_name', 'course_duration', 'seat']