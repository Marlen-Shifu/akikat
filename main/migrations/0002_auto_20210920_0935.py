# Generated by Django 3.2.7 on 2021-09-20 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookModel',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='CategoryModel',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='SubCategoryModel',
            new_name='SubCategory',
        ),
    ]
