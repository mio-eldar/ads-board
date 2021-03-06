# Generated by Django 3.1.5 on 2021-02-05 16:42

import ad.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad', '0004_auto_20210203_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('currency', models.CharField(choices=[('SOM', 'SOM'), ('USD', 'USD')], default='SOM', max_length=3)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone number')),
                ('hide_phone_number', models.BooleanField(default=False, verbose_name='hide phone number')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='email address')),
                ('main_image', models.ImageField(upload_to=ad.models.upload_image_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='AdvertisementImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=ad.models.upload_image_path)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ad.advertisement')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ad.category'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.city'),
        ),
    ]
