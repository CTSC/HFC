# Generated by Django 3.0.6 on 2020-05-08 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0002_auto_20200501_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('Center', 'Center'), ('Chapter', 'Chapter')], max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('coordinator_name', models.CharField(max_length=100)),
                ('coordinator_email', models.EmailField(max_length=254)),
                ('coordinator_mobile', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('project_link', models.URLField()),
                ('project_icon', models.ImageField(upload_to='')),
                ('project_desc', models.TextField()),
                ('website_link', models.URLField()),
                ('goal', models.TextField()),
                ('funded_by', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Problem_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('summary', models.TextField()),
                ('background_info', models.TextField()),
                ('related_link', models.URLField()),
                ('proposed_solution', models.TextField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('New / Open', 'New / Open'), ('Work In Progress', 'Work In Progress'), ('Resolved', 'Resolved')], max_length=100)),
                ('partner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HFCCore.Partner')),
            ],
            options={
                'verbose_name': 'Problem_Statement',
                'verbose_name_plural': 'Problem_Statements',
            },
        ),
    ]
