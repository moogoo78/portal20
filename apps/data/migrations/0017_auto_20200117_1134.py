# Generated by Django 3.0.1 on 2020-01-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_auto_20200117_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='status',
            field=models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], max_length=10, verbose_name='status'),
        ),
    ]
