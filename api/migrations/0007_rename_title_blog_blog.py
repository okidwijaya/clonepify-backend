# Generated by Django 5.0.4 on 2024-06-02 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_blog_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='blog',
        ),
    ]
