# Generated by Django 3.0.2 on 2020-01-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_restaurant_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
