# Generated by Django 3.2.7 on 2021-10-25 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_article_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='slug',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
