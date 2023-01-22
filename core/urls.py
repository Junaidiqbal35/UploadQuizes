from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExamListView.as_view(), name='exam-list'),
    path('detail/<int:pk>/', views.ExamFilesDetailView.as_view(), name='exam-detail'),
    path('submit/exam/<int:pk>/', views.SubmitAssignment.as_view(), name='submit_exam')
]
