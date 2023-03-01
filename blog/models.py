from django.db import models

from accounts.models import Account
from tinymce.models import HTMLField

class Article(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=False)
    description = HTMLField(null=False)
    tags = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
