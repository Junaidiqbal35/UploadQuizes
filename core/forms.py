from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.models import ExamResult


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=255, required=True)

    # password = forms.CharField(widget=PasswordInput(), validators=[validate_password])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SubmitAssignmentsForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['submit_files']
