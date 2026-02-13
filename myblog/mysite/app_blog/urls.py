# app_blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
 path(r'', views.HomePageView.as_view()),
]