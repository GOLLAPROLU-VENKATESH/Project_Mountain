from django.db import models


class Blogs(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    para1 = models.TextField(max_length=500)
    para2 = models.TextField(max_length=500)
    phone_number = models.IntegerField(default=1234567890)
    description = models.CharField(max_length=200)