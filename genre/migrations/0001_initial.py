# Generated by Django 4.2.5 on 2023-09-13 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('collcover', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('typ', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('piececover', models.CharField(max_length=1000)),
                ('collectiom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.collection')),
            ],
        ),
    ]
