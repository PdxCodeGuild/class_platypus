# Generated by Django 2.1.2 on 2018-10-03 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20181003_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='completed',
        ),
    ]