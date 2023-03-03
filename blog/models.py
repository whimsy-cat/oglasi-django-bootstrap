from django.db import models

from accounts.models import Account
from tinymce.models import HTMLField
from django.utils import timezone


class ArticleCategory(models.Model):
    ARTICLE_TYPE_CHOICES = (
        ('Blog', 'Blog'),
        ('News', 'News'),
    )
        
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    for_article_type = models.CharField(max_length=4, choices=ARTICLE_TYPE_CHOICES, default='Blog')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Article Categories"


class Article(models.Model):
    ARTICLE_TYPE_CHOICES = (
        ('Blog', 'Blog'),
        ('News', 'News'),
    )
        
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    cover = models.FileField(max_length=255, upload_to='blog', null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=False)
    description = HTMLField(null=False)
    timestamp = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=255, null=True)
    article_type = models.CharField(max_length=4, choices=ARTICLE_TYPE_CHOICES, default='Blog')

    def __str__(self):
        return self.title
