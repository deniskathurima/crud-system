# Generated by Django 4.2.5 on 2025-01-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('id_no', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=100)),
            ],
        ),
    ]
