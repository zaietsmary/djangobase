# app_blog/urls.py
from django.urls import path
from . import views
from .views import (HomePageView, ArticleDetail, ArticleList, ArticleCategoryList)

urlpatterns = [
path('', views.HomePageView.as_view(), name='home'),
path(r'articles', ArticleList.as_view(), name='articleslist'),
path(r'articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>/', ArticleDetail.as_view(), name='news-detail'
)
]