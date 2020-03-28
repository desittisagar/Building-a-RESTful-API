from django.urls import path
from .views import SubjectListView, SubjectDetailView

app_name = "courses"

urlpatterns = [
    path('subject/', SubjectListView.as_view(), name = 'subject_list'),
    path('subject/<pk>/', SubjectDetailView.as_view(), name = 'subject_detail'),
]