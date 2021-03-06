# Generated by Django 2.1.7 on 2019-04-18 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Machine_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type_name', models.CharField(db_index=True, max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.Machine_type'),
        ),
    ]
