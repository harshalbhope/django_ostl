# Generated by Django 2.0.2 on 2018-03-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_book_format_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Book_logo',
            field=models.FileField(upload_to=''),
        ),
    ]