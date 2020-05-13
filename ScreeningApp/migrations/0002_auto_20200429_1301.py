# Generated by Django 2.2.4 on 2020-04-29 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertise',
            name='expertise',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='expertise_area',
            name='area_of_expertise',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='screenings',
            name='candidate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Candidate', verbose_name='Candidate Name'),
        ),
    ]