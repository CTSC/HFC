# Generated by Django 2.2.4 on 2020-05-18 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0009_auto_20200518_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='area_of_expertise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Expertise'),
        ),
    ]
