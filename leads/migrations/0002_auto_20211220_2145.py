# Generated by Django 3.2.9 on 2021-12-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='agent',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]