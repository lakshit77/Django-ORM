# Generated by Django 4.2.2 on 2023-06-29 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_orm_app', '0002_alter_blog_author'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='author_model',
        ),
        migrations.AlterModelTable(
            name='blog',
            table='blog_model',
        ),
    ]