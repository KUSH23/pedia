# Generated by Django 2.2.1 on 2019-07-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190716_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]