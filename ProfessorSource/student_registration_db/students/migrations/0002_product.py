# Generated by Django 3.2.8 on 2021-11-06 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pdescription', models.CharField(max_length=100)),
                ('pimagepath', models.CharField(max_length=100)),
                ('pcategory', models.CharField(max_length=20)),
                ('pprice', models.FloatField()),
            ],
        ),
    ]
