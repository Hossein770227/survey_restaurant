# Generated by Django 5.1.3 on 2024-11-29 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_ourstrengths_alter_food_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourstrengths',
            old_name='Strength',
            new_name='title',
        ),
    ]
