# Generated by Django 3.2.7 on 2021-09-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0011_alter_ticket_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]