# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='login_register/avatar/default/default.jpg', upload_to='login_register/avatar/')),
                ('resize', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_image', to='login_register.User')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_image', to='user_profile.Images')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(default=False)),
                ('occupation', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('street_number', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('longtitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('about_me', models.CharField(max_length=500)),
                ('distAway', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='login_register.User')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='match_profile', to='user_profile.Profile'),
        ),
        migrations.AddField(
            model_name='match',
            name='this_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='match_user', to='login_register.User'),
        ),
    ]
