# Generated by Django 4.0.3 on 2022-04-10 11:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qpd_api', '0002_remove_job_settings_remove_job_strategy_job_gamma_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='id',
        ),
        migrations.AddField(
            model_name='job',
            name='jobid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]