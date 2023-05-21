# Generated by Django 4.2.1 on 2023-05-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('compound', models.TextField()),
                ('size', models.TextField(max_length=4, verbose_name='Размер')),
                ('manufacturer', models.TextField(verbose_name='Производитель')),
                ('availability', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3, verbose_name='Есть ли в наличии?')),
                ('which_branch', models.TextField(choices=[('ТРЦ "АЗИЯ МОЛЛ', 'ТРЦ "АЗИЯ МОЛЛ'), ('Дордой Плаза 1. 1-этаж, бутикD2 ', 'Дордой Плаза 1. 1-этаж, бутикD2 ')], verbose_name='В каком филиале')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]