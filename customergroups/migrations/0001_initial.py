# Generated by Django 2.2.1 on 2019-07-15 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30, unique=True)),
                ('group_prefix', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Country')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.District')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.State')),
            ],
            options={
                'verbose_name': 'Customer Group',
                'verbose_name_plural': 'Customer Groups',
            },
        ),
    ]
