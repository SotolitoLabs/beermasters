# Generated by Django 2.2.2 on 2019-06-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0006_contesttable_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestscoresheet',
            name='total_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
