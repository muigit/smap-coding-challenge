# Generated by Django 2.2.15 on 2023-09-10 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggregateUserDailyConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_consumption', models.FloatField()),
                ('average_consumption', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.User')),
            ],
            options={
                'unique_together': {('user', 'date')},
            },
        ),
    ]