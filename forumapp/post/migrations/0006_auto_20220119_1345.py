# Generated by Django 3.2.5 on 2022-01-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comment_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]