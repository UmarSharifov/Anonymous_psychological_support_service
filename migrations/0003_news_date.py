# Generated by Django 3.1.7 on 2021-04-08 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psyco', '0002_advice_horoscope_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 8)),
        ),
    ]
