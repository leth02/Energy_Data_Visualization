# Generated by Django 3.0.2 on 2020-01-13 22:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0002_auto_20200113_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('electric_use', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Electric',
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for each room of the building', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='energy',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='energy.Room'),
        ),
    ]
