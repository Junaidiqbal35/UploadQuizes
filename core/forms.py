from django import forms

from core.models import ExamResult


class SubmitAssignmentsForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['submit_files']
