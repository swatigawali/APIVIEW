from django.urls import path
from .views import EmployeeAPIview

urlpatterns=[
    path('emp/',EmployeeAPIview.as_view()),
    path('emp/<int:pk>/',EmployeeAPIview.as_view())
]