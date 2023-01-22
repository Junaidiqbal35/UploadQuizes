from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import SubmitAssignmentsForm, CreateUserForm
from .models import UploadQuiz, ExamResult, ExamType


class SignUpView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ExamListView(ListView):
    model = ExamType
    template_name = 'exam/exam_type.html'
    queryset = ExamType.objects.all()
    context_object_name = 'exam_type'


class ExamFilesDetailView(DetailView):
    model = UploadQuiz
    template_name = 'exam/exam_files.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_detail'] = get_object_or_404(self.model, exam_type__id=self.kwargs['pk'])
        context['submit_assignment'] = SubmitAssignmentsForm

        return context


class SubmitAssignment(LoginRequiredMixin, CreateView):
    model = ExamResult
    form_class = SubmitAssignmentsForm
    template_name = 'exam/submit_exam.html'

    def form_valid(self, form):
        exam_obj = UploadQuiz.objects.get(id=self.kwargs['pk'])
        form.instance.exam = exam_obj
        form.instance.submit_by = self.request.user
        form.save()
        return redirect('exam-detail', exam_obj.id)

    def form_invalid(self, form):
        print(form.errors)


class StudentSubmitAssignmentView(LoginRequiredMixin, ListView):
    model = ExamResult
    template_name = 'user_submitted_assignment.html'
    context_object_name = 'user_assignments'

    def get_queryset(self):
        return self.model.objects.filter(submit_by__email=self.request.user.email)
