# Generated by Django 4.2.5 on 2023-10-23 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_test_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='img',
        ),
    ]
