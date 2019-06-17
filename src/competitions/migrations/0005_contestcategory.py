# Generated by Django 2.2.2 on 2019-06-17 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_auto_20190616_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.Contest')),
            ],
        ),
    ]
