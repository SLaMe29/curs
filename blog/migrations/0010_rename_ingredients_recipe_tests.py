# Generated by Django 3.2.4 on 2023-10-04 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20231004_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients',
            new_name='tests',
        ),
    ]
