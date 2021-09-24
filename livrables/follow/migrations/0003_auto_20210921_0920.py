# Generated by Django 3.2.7 on 2021-09-21 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('follow', '0002_auto_20210920_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
        migrations.AddField(
            model_name='follow',
            name='followed_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]