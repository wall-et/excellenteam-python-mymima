# Generated by Django 2.1.5 on 2019-01-13 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='publisher_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]