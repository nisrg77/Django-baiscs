from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList,name="employeeList"),
    path('employeeFilter/', views.employeeFilter,name="employeeFilter"),
]