# Generated by Django 3.1.2 on 2020-10-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201027_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
