# Generated by Django 5.2 on 2025-05-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20250416_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
