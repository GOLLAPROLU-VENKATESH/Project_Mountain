# Generated by Django 4.0.6 on 2022-07-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_number',
            field=models.IntegerField(default=1234567890),
        ),
    ]
