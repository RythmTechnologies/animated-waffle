# Generated by Django 5.0.2 on 2024-02-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Logo Adı')),
                ('image', models.ImageField(upload_to='logo/', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Site Logo',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='Anasayfa İçerik Başlık')),
                ('short_title', models.CharField(max_length=50, verbose_name='Anasayfa İçerik Kısa Yazı')),
                ('image', models.ImageField(upload_to='anasayfa/', verbose_name='Anasayfa İçerik Resim')),
            ],
            options={
                'verbose_name': 'Ana Sayfa',
                'verbose_name_plural': 'Ana Sayfa Tasarımları',
            },
        ),
    ]