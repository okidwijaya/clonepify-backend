# Generated by Django 5.0.4 on 2024-06-02 02:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_title_blog_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogpost', to='api.blog'),
        ),
    ]