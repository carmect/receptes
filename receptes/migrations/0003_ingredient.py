# Generated by Django 2.1.7 on 2019-03-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptes', '0002_auto_20190314_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
            ],
        ),
    ]
