# Generated by Django 3.2.3 on 2021-06-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_tasks_task_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_details',
            name='TaskName',
            field=models.CharField(max_length=90),
        ),
    ]