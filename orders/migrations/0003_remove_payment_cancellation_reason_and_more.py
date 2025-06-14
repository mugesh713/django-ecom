# Generated by Django 5.2 on 2025-06-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_payment_cancellation_reason_payment_is_cancelled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='cancellation_reason',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='is_cancelled',
        ),
        migrations.AddField(
            model_name='order',
            name='cancellation_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
