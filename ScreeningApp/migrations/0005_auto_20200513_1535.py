# Generated by Django 2.2.4 on 2020-05-13 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0004_auto_20200513_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='area_of_expertise',
            new_name='category_of_expertise',
        ),
    ]
