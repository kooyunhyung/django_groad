# Generated by Django 4.0.6 on 2022-11-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0025_user_gu_step_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gu_step_number',
            field=models.FloatField(null=True),
        ),
    ]
