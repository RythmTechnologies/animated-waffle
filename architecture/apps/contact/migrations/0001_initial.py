# Generated by Django 5.0.2 on 2024-02-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.TextField(verbose_name='Şirket Adresi')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon Numarası')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Adresi')),
            ],
            options={
                'verbose_name': 'Şirket',
                'verbose_name_plural': 'Şirket Bilgisi',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Adı')),
                ('surname', models.CharField(max_length=50, verbose_name='Soyadı')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Adresi')),
                ('message', models.TextField(verbose_name='Mesaj İçeriği')),
            ],
            options={
                'verbose_name': 'İletişim',
                'verbose_name_plural': 'İletişimler',
            },
        ),
    ]