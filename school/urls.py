from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main page (lists students and teachers)

    # Student URLs
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:pk>/', views.student_read, name='student_read'),  # Detail view
    path('student/<int:pk>/update/', views.student_update, name='student_update'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # Teacher URLs
    path('teacher/create/', views.teacher_create, name='teacher_create'),
    path('teacher/<int:pk>/', views.teacher_read, name='teacher_read'),  # Detail view
    path('teacher/<int:pk>/update/', views.teacher_update, name='teacher_update'),
    path('teacher/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
]