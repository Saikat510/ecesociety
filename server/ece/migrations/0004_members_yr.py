# Generated by Django 3.0.7 on 2020-06-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ece', '0003_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='yr',
            field=models.IntegerField(null=True),
        ),
    ]
