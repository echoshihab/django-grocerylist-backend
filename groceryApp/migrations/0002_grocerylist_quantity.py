# Generated by Django 2.1.2 on 2019-04-02 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocerylist',
            name='quantity',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
