# Generated by Django 3.1.3 on 2023-02-03 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230203_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_grade',
            new_name='grade',
        ),
    ]
