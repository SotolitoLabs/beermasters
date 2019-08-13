# Generated by Django 2.2.2 on 2019-08-13 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0015_auto_20190811_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestCategoryStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.ContestCategory')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.BJCPstyle')),
            ],
        ),
    ]
