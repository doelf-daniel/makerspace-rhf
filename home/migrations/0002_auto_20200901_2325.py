# Generated by Django 3.1 on 2020-09-01 23:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 23, 25, 18, 280782, tzinfo=utc), verbose_name='Post date'),
        ),
    ]