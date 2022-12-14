# Generated by Django 4.1.2 on 2022-11-08 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('method', models.CharField(choices=[('GE', 'Get request'), ('HE', 'Head request'), ('PO', 'Post request'), ('PU', 'Put request'), ('DE', 'Delete request'), ('CO', 'Connect request'), ('OP', 'Options request'), ('TR', 'Trace request'), ('PA', 'Path request')], max_length=2)),
                ('timestamp', models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 8, 15, 26, 20, 409800))),
                ('values', models.JSONField(default={})),
            ],
        ),
    ]
