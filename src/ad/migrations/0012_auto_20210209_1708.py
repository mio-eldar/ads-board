# Generated by Django 3.1.5 on 2021-02-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0011_auto_20210208_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='main_image',
        ),
        migrations.AddField(
            model_name='advertisementimage',
            name='is_main',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
