# Generated by Django 3.2.9 on 2022-01-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220111_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(null=True, related_name='blog', to='blog.Category'),
        ),
    ]
