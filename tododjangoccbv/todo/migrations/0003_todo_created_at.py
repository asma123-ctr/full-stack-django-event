# Generated by Django 3.0.7 on 2021-04-18 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
