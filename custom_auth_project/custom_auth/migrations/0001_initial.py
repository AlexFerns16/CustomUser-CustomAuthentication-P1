# Generated by Django 4.2.4 on 2024-02-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
