# Generated by Django 2.0.2 on 2018-03-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180308_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_format',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]