# Generated by Django 2.2.4 on 2022-09-18 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojos_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojos',
            name='desc',
        ),
    ]
