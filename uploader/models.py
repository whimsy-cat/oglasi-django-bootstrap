import random
import string
from django.db import models

def generate_random_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

# Create your models here.
class DropBox(models.Model):
    id = models.CharField(max_length=16, default=generate_random_code, db_index=True, primary_key=True)
    file = models.FileField(max_length=100, upload_to='listings')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Drop Boxes'
