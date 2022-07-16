from django.db import models


class ContactUsc(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(default=1234567890)
    description = models.CharField(max_length=200)

    def register(self):
        self.save()
