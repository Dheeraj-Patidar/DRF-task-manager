# Generated by Django 5.1.7 on 2025-03-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_alter_task_assigned_to_alter_task_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
