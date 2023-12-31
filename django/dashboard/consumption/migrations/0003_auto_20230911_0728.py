# Generated by Django 2.2.15 on 2023-09-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0002_aggregateuserdailyconsumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggregateuserdailyconsumption',
            name='date',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='consumption',
            name='datetime',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.CharField(db_index=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='tariff',
            field=models.CharField(db_index=True, max_length=2),
        ),
    ]
