# Generated by Django 4.2.3 on 2023-09-06 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_alter_advert_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advert',
            new_name='Advertisement',
        ),
    ]
