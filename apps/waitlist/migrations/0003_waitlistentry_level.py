# Generated by Django 3.0.8 on 2020-07-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0002_auto_20200724_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Class Level'),
        ),
    ]
