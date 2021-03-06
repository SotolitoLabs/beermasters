# Generated by Django 2.2.2 on 2019-06-16 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apperance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('color', models.IntegerField()),
                ('transp', models.IntegerField()),
                ('other', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Aroma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('malt', models.IntegerField()),
                ('hop', models.IntegerField()),
                ('fermentation', models.IntegerField()),
                ('other', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContestScoreSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_ingredients', models.CharField(max_length=200)),
                ('bottle_insp', models.NullBooleanField()),
                ('bottle_insp_comment', models.TextField()),
                ('overall_score', models.IntegerField()),
                ('overall_comment', models.TextField()),
                ('style', models.IntegerField()),
                ('technical', models.IntegerField()),
                ('intangilble', models.IntegerField()),
                ('apperance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.Apperance')),
                ('aroma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.Aroma')),
            ],
        ),
        migrations.CreateModel(
            name='DescriptorDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('malt', models.IntegerField()),
                ('hop', models.IntegerField()),
                ('bitterness', models.IntegerField()),
                ('fermentation', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('final', models.IntegerField()),
                ('other', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mouthfeel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('body', models.IntegerField()),
                ('carbonation', models.IntegerField()),
                ('warmth', models.IntegerField()),
                ('creaminess', models.IntegerField()),
                ('astringency', models.IntegerField()),
                ('other', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContestScoreSheetDescriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.DescriptorDefinition')),
                ('score_sheet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.ContestScoreSheet')),
            ],
        ),
        migrations.AddField(
            model_name='contestscoresheet',
            name='flavor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.Flavor'),
        ),
        migrations.AddField(
            model_name='contestscoresheet',
            name='mouthfee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.Mouthfeel'),
        ),
        migrations.AddField(
            model_name='contestscoresheet',
            name='table_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competitions.ContestTableItem'),
        ),
    ]
