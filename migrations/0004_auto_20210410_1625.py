# Generated by Django 3.1.7 on 2021-04-10 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psyco', '0003_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='horoscope',
            name='element',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='horoscope',
            name='element_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='horoscope',
            name='interval_end',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='horoscope',
            name='interval_start',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 10)),
        ),
    ]