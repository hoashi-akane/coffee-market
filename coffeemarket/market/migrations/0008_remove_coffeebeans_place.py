# Generated by Django 3.0.3 on 2020-04-14 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20200414_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeebeans',
            name='place',
        ),
    ]