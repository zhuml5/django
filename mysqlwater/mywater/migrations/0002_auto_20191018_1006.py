# Generated by Django 2.2.6 on 2019-10-18 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cod',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='cond',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='do',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='nh3',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='orp',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='ph',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='temp',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='tp',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='zd',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='detial',
            field=models.CharField(default=0, max_length=100),
        ),
    ]