# Generated by Django 5.0.1 on 2024-01-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Emp_salary',
            field=models.FloatField(),
        ),
    ]
