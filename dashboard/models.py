from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Short_URL(models.Model):
    short_url = models.CharField(max_length=50, unique=True)
    long_url = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    clicked = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
