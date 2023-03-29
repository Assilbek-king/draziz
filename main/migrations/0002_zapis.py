# Generated by Django 4.0.4 on 2023-03-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('service', models.CharField(blank=True, max_length=300)),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=True)),
            ],
        ),
    ]
