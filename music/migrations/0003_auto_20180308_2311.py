# Generated by Django 2.0.2 on 2018-03-08 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180308_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Publisher',
            new_name='Book_title',
        ),
        migrations.RenameField(
            model_name='book_format',
            old_name='file_type',
            new_name='Publisher',
        ),
        migrations.RenameField(
            model_name='book_format',
            old_name='Book_name',
            new_name='book',
        ),
    ]