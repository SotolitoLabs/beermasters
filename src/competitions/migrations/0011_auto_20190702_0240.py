# Generated by Django 2.2.2 on 2019-07-02 02:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0010_populate_styles'),
    ]

    operations = [
        migrations.CreateModel(
            name='BJCPcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of addition')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BJCPstyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of addition')),
                ('name', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.BJCPcategory')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='style',
            field=models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.BJCPstyle'),
        ),
    ]
