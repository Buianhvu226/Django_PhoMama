# Generated by Django 5.0.6 on 2024-05-21 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_remove_orders_arrive_time_remove_orders_chef_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='Role',
        ),
    ]
