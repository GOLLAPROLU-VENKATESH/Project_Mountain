from django.db import models


class ContactUs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(default=1234567890)
    name_of_event = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def register(self):
        self.save()
