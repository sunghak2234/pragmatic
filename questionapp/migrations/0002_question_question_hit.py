# Generated by Django 3.2.8 on 2021-10-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
