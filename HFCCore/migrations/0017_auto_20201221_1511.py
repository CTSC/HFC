# Generated by Django 2.2.4 on 2020-12-21 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0016_community_member_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem_statement',
            name='issue_area',
        ),
        migrations.RemoveField(
            model_name='problem_statement',
            name='issue_area_slug',
        ),
    ]
