from django.test import TestCase
from django.utils import timezone

from .models import Category, Article


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category = self.category
        self.assertEqual(category.get_absolute_url(), '/articles/category/innovations')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Innovations')


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category='Innovations', slug='innovations')

    def test_create_article_model(self):
        article = Article.objects.create(
            title='My Blog',
            slug='myblog',
            description='My Blog Description',
            category=self.category,
            pub_date=timezone.now()
        )
        self.assertEqual(article.title, 'My Blog')
        self.assertEqual(article.category, self.category)
        self.assertEqual(article.slug, 'myblog')
