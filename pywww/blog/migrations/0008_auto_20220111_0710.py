# Generated by Django 3.2.9 on 2022-01-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('blog', '0007_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='blog', to='tags.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='blog', to='blog.Category'),
        ),
    ]
