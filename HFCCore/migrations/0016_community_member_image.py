# Generated by Django 2.2.4 on 2020-11-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0015_community_organization_organization_name_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='community_member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]