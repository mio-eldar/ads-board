# Generated by Django 3.1.5 on 2021-02-07 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad', '0005_auto_20210205_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='likes',
            field=models.ManyToManyField(related_name='liked_ads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='price'),
        ),
    ]
