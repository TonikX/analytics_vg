# Generated by Django 2.0.5 on 2019-12-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataprocessing', '0008_auto_20191227_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='item2',
        ),
        migrations.AddField(
            model_name='relation',
            name='item2',
            field=models.ManyToManyField(related_name='item2', to='dataprocessing.Items', verbose_name='Элемент РПД'),
        ),
    ]