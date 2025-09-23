from django.test import TestCase
from django.urls import reverse, resolve
import datetime

from .models import Category, Article
from .views import HomePageView, ArticleCategoryList, ArticleDetail, ArticleList

class HomeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category="Test Category", slug="test-category")
        cls.article = Article.objects.create(
            title="Test Article",
            slug="test-article",
            description="Description",
            category=cls.category,
            pub_date=datetime.date(2025, 9, 23)  # приклад дати
        )

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articleslist_view_status_code(self):
        url = reverse('articleslist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articlescategorylist_view_status_code(self):
        url = reverse('articles-category-list', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_newsdetail_view_status_code(self):
        url = reverse('news-detail', kwargs={
            'year': self.article.pub_date.year,
            'month': self.article.pub_date.month,
            'day': self.article.pub_date.day,
            'slug': self.article.slug
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_view_displays_correct_category(self):
        url = reverse('articles-category-list', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertContains(response, self.category.category)
