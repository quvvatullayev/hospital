# Generated by Django 4.2.5 on 2023-10-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_name_customermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
