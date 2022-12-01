from django.db import models

from accounts.models import Account


class Article(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    tags = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
