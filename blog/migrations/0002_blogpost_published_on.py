# Generated by Django 4.2.4 on 2024-01-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published_on',
            field=models.DateTimeField(null=True),
        ),
    ]
