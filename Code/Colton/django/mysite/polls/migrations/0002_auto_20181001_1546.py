# Generated by Django 2.1.2 on 2018-10-01 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pup_date',
            new_name='pub_date',
        ),
    ]
