# Generated by Django 5.0 on 2024-01-29 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_project_options_project_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created_at']},
        ),
    ]
