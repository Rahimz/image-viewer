# Generated by Django 5.0 on 2024-02-08 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_file',
        ),
    ]