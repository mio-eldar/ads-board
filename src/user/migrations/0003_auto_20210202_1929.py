# Generated by Django 3.1.5 on 2021-02-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210130_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
