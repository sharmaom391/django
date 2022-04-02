from django.db import models

# Create your models here.
class Short_URL(models.Model):
    short_url=models.CharField(max_length=20)
    long_url=models.URLField("URL",unique=True)
