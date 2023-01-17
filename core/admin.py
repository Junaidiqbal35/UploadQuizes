from django.contrib import admin
from .models import ExamType, UploadQuiz, ExamResult
# Register your models here.
admin.site.register(ExamType)
admin.site.register(UploadQuiz)
admin.site.register(ExamResult)