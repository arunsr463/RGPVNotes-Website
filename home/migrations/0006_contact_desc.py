# Generated by Django 3.2.2 on 2021-06-01 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_login_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]