from django.db import models
from uuid import uuid4

# Create your models here.
class Posts(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=20)
    created_datetime = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)
