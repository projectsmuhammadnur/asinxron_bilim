# Generated by Django 4.2.7 on 2023-12-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('chat_id', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('step', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Telegram User',
                'verbose_name_plural': 'Telegram Users',
            },
        ),
    ]
