# Generated by Django 3.2.2 on 2021-06-01 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='login',
            name='emailid',
            field=models.EmailField(max_length=254),
        ),
    ]
