# Generated by Django 5.0.6 on 2024-06-21 03:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('order_status', models.CharField(choices=[('готовится', 'Готовится'), ('готов', 'Готов')], default='готовится', max_length=255, verbose_name='Статус заказа')),
                ('room_number', models.CharField(max_length=255, verbose_name='Номер комнаты')),
                ('amount_clients', models.IntegerField(verbose_name='Количество клиентов')),
                ('hotel_services', models.CharField(max_length=255, verbose_name='Услуги')),
                ('payment_status', models.CharField(choices=[('принят', 'Принят'), ('оплачен', 'Оплачен')], default='принят', max_length=255, verbose_name='Статус оплаты')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
            options={
                'verbose_name': 'Смена',
                'verbose_name_plural': 'Смены',
            },
        ),
        migrations.CreateModel(
            name='OrderUserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Связанный заказ',
                'verbose_name_plural': 'Связанные заказы',
            },
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.shift')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Связанная смена',
                'verbose_name_plural': 'Связанные смены',
            },
        ),
    ]
