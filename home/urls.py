from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check-date/<str:dateStr>/', views.check_date, name='check_date'),
]