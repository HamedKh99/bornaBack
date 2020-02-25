from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('haftkhanpre/', views.HaftkhanPreView.as_view()),
    path('haftkhansignup/', views.HaftkhanSignupView.as_view())
]