# Generated by Django 2.1.7 on 2019-03-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receptes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recepta',
            old_name='titol',
            new_name='title',
        ),
    ]
