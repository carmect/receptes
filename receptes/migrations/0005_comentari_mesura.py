# Generated by Django 2.1.7 on 2019-03-19 11:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('receptes', '0004_auto_20190319_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('data_creacio', models.DateTimeField(default=django.utils.timezone.now)),
                ('recepta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentaris', to='receptes.Recepta')),
            ],
        ),
        migrations.CreateModel(
            name='Mesura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
    ]
