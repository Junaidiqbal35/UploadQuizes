from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# Hi - I need an exam website where we post a question and multiple students can upload files and folders.


class ExamType(models.Model):
    class Meta:
        verbose_name = "Exam Tyoe"
        verbose_name_plural = "Exam Type"
        ordering = ['id']

    title = models.CharField(max_length=255, default="Exam Type", verbose_name="Exam Title")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UploadQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    exam_description = models.TextField()
    exam_folder = models.FileField(verbose_name='Exam Folder', upload_to='exams',
                                   help_text='Upload Zip Folder of files')

    total_time = models.CharField(max_length=255, default='1 hour')
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.exam_type.title


class ExamResult(models.Model):
    exam = models.ForeignKey(UploadQuiz, on_delete=models.CASCADE)
    submit_by = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()

    def __str__(self):
        return self.submit_by
