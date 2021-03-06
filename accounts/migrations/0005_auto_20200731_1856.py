# Generated by Django 3.0.8 on 2020-07-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200728_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_link',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='tableuser',
            name='username',
            field=models.TextField(default='none'),
        ),
    ]
