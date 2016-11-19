# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-19 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='any text you want', max_length=120, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=portfolio.models.about_me_upload_location, verbose_name='my image')),
                ('about_me', models.TextField(verbose_name='about me')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250, verbose_name='subject')),
                ('sender', models.EmailField(max_length=254, verbose_name='sender')),
                ('message', models.TextField(verbose_name='message')),
                ('copy', models.BooleanField(default=False, verbose_name='copy')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Uncategorized', max_length=50, verbose_name='category')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, default='', max_length=4096, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='updated')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'portfolio category',
                'verbose_name_plural': 'portfolio categories',
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('width_field', models.IntegerField(default=0, verbose_name='width field')),
                ('height_field', models.IntegerField(default=0, verbose_name='height field')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=portfolio.models.upload_location, verbose_name='image', width_field='width_field')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('draft', models.BooleanField(default=False, verbose_name='draft')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='updated')),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(default='Uncategorized', on_delete=django.db.models.deletion.PROTECT, related_name='image', to='portfolio.PortfolioCategory', verbose_name='category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'portfolio image',
                'verbose_name_plural': 'portfolio images',
            },
        ),
        migrations.CreateModel(
            name='PortfolioSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='any text you want', max_length=120, verbose_name='name')),
                ('image', models.ImageField(blank=True, null=True, upload_to=portfolio.models.slider_upload_location, verbose_name='image')),
                ('image_text', models.CharField(blank=True, help_text='comment 30 characters long', max_length=30, null=True, verbose_name='image text')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='portfolioimage',
            index_together=set([('id', 'slug')]),
        ),
    ]