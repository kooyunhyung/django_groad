# Generated by Django 4.0.6 on 2022-11-15 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0024_cafe_list_gcl_course_lodging_list_gll_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gu_step_number',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)], verbose_name='걸음'),
        ),
    ]